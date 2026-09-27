import {views,people,loadTemplates,imageFrom,renderPolo,renderPerson,garmentImage,sampleArtwork,pointInPrint} from './render.js';
import {chestPlacement} from './geometry.js';
import {acceptsTryOn} from './session-guard.js';
const $=id=>document.getElementById(id);
const fabrics={cotton:'100% cotton',blend:'Cotton/polyester 65/35'};
const palette=[['Forest','#264c3f'],['Ivory','#eee9dc'],['Ink','#263442'],['Clay','#a77861'],['Sage','#9ca98c'],['Black','#30302f']];
let draft={colour:palette[0][1],fabric:'cotton',side:'front',revision:0,assets:[],selected:null};
let tab='design',viewIndex=0,presetIndex=0,person=null,result=null,review=null,session=0,personToken=0,engine=null,bgToken=0,tryonToken=0;
let requestController=null,bgController=null,drag=null,generating=false,showOriginal=false;
let templatesReady=false;
const editor=$('editor-canvas'),mockup=$('mockup-canvas'),personCanvas=$('person-canvas');personCanvas.width=512;personCanvas.height=1024;
function message(text,error=false){$('status').textContent=text;$('status').classList.toggle('error',error);}
function selected(){return draft.assets.find(a=>a.id===draft.selected&&a.side===draft.side);}
function changed(){draft.revision++;tryonToken++;result=null;showOriginal=false;if(generating){requestController?.abort();generating=false;$('generation-overlay').hidden=true;}render();}
function render(){
  if(!templatesReady)return;
  renderPolo(editor,draft,draft.side==='front'?0:4,true);renderPolo(mockup,draft,viewIndex);renderPerson(personCanvas,draft,presetIndex);
  $('fabric').value=draft.fabric;$('intro-fabric').textContent=fabrics[draft.fabric];$('product-material').textContent=fabrics[draft.fabric]+' · Regular fit';
  for(const id of ['chest-left','chest-right'])$(id).disabled=draft.side!=='front';$('chest-note').hidden=draft.side!=='front';
  $('surface-tag').textContent=draft.side==='front'?'MẶT TRƯỚC':'MẶT SAU';$('colour-name').textContent=palette.find(p=>p[1]===draft.colour)[0];
  $('view-tag').textContent=views[viewIndex].name.toUpperCase();$('view-index').textContent=`0${viewIndex+1} / 06`;$('asset-count').textContent=`${draft.assets.length} / 5`;
  document.querySelectorAll('[data-side]').forEach(b=>b.setAttribute('aria-pressed',b.dataset.side===draft.side));
  document.querySelectorAll('[data-colour]').forEach(b=>b.setAttribute('aria-pressed',b.dataset.colour===draft.colour));
  const list=$('asset-list');list.replaceChildren();
  for(const a of draft.assets.filter(a=>a.side===draft.side)){
    const row=document.createElement('div');row.className='asset'+(draft.selected===a.id?' selected':'');
    const img=new Image();img.src=a.active;img.alt='';
    const select=document.createElement('button');select.className='asset-select';const name=document.createElement('span');name.textContent=a.name;const info=document.createElement('small');info.textContent=`${Math.round(a.w)} × ${Math.round(a.h)} mm`;select.append(name,info);select.onclick=()=>{draft.selected=a.id;render();};
    const remove=document.createElement('button');remove.className='asset-delete';remove.textContent='×';remove.setAttribute('aria-label','Bỏ hình '+a.name);remove.onclick=()=>{draft.assets=draft.assets.filter(x=>x.id!==a.id);draft.selected=draft.assets.find(x=>x.side===draft.side)?.id||null;changed();};row.append(img,select,remove);list.append(row);
  }
  const a=selected();$('placement').hidden=!a;
  if(a){for(const[key,id]of[['x','pos-x'],['y','pos-y'],['w','pos-w'],['h','pos-h']]){if(document.activeElement!==$(id))$(id).value=Math.round(a[key]);}$('restore-art').hidden=a.active===a.original;}
  document.querySelectorAll('#mockup-thumbs canvas').forEach((c,i)=>{renderPolo(c,draft,i);c.parentElement.setAttribute('aria-pressed',i===viewIndex);});
  document.querySelectorAll('#preset-list canvas').forEach((c,i)=>{renderPerson(c,draft,i);c.parentElement.setAttribute('aria-pressed',!person&&i===presetIndex);});
  $('person-card').hidden=!person;$('person-thumbnail').src=person?.src||'';personCanvas.hidden=!!person;
  $('personal-result').hidden=!person;
  if(person){$('personal-result').src=!showOriginal&&result?result.image:person.src;$('person-tag').textContent=result&&!showOriginal?'ẢNH THỬ ÁO · AI':'ẢNH CỦA BẠN';$('person-caption').textContent=result&&!showOriginal?'Ảnh AI minh họa · Kiểm tra lại chi tiết hình in':'Ảnh đầu vào · Chưa thay áo';}
  else{$('personal-result').removeAttribute('src');$('person-tag').textContent=`MẪU ${people[presetIndex].name.toUpperCase()} · MOCKUP`;$('person-caption').textContent='Mẫu tổng hợp · Hình in ghép theo thiết kế hiện tại';}
  $('show-original').hidden=!result||!person;$('show-original').textContent=showOriginal?'Xem kết quả AI':'Xem ảnh gốc';
  $('generate').disabled=!person||generating||(!engine?.available||!$('external-consent').checked);
  $('generate').textContent=generating?'Đang xử lý…':'✧ Thử áo trên tôi';
}
function switchTab(next){tab=next;for(const mode of['design','mockups','tryon']){$('panel-'+mode).hidden=mode!==tab;$('tab-'+mode).setAttribute('aria-selected',mode===tab);$('tab-'+mode).tabIndex=mode===tab?0:-1;}message('');render();if(tab==='tryon')refreshEngine().catch(()=>{});}
document.querySelectorAll('[data-tab]').forEach(b=>{b.onclick=()=>switchTab(b.dataset.tab);b.onkeydown=e=>{if(e.key==='ArrowLeft'||e.key==='ArrowRight'){const modes=['design','mockups','tryon'];const next=modes[(modes.indexOf(tab)+(e.key==='ArrowRight'?1:2))%3];switchTab(next);$('tab-'+next).focus();}};});
$('fabric').onchange=()=>{draft.fabric=$('fabric').value;changed();message('Đã chọn vải '+fabrics[draft.fabric]+'.');};
for(const [id,kind] of [['chest-left','left'],['chest-right','right'],['centre-art','centre']])$(id).onclick=()=>{const a=selected();if(!a)return;const ratio=a.image.naturalHeight/a.image.naturalWidth;if(kind==='centre'){a.w=Math.min(140,200/ratio);a.h=a.w*ratio;a.x=(300-a.w)/2;a.y=100;}else Object.assign(a,chestPlacement(kind,ratio));changed();message(kind==='centre'?'Đã đặt hình giữa áo.':'Đã đặt logo ở ngực '+(kind==='left'?'trái':'phải')+' theo người mặc.');};
$('go-mockups').onclick=()=>switchTab('mockups');$('back-edit').onclick=()=>switchTab('design');
for(const[name,colour]of palette){const b=document.createElement('button');b.dataset.colour=colour;b.style.background=colour;b.title=name;b.setAttribute('aria-label','Màu '+name);b.onclick=()=>{draft.colour=colour;changed();};$('colours').append(b);}
document.querySelectorAll('[data-side]').forEach(b=>b.onclick=()=>{draft.side=b.dataset.side;draft.selected=draft.assets.find(a=>a.side===draft.side)?.id||null;render();});
for(let i=0;i<views.length;i++){const b=document.createElement('button'),c=document.createElement('canvas'),s=document.createElement('span');c.width=192;c.height=192;s.textContent=views[i].name;b.setAttribute('aria-label','Xem '+views[i].name);b.append(c,s);b.onclick=()=>{viewIndex=i;render();};$('mockup-thumbs').append(b);}
for(let i=0;i<people.length;i++){const b=document.createElement('button'),c=document.createElement('canvas'),s=document.createElement('span');c.width=100;c.height=200;s.textContent=people[i].name;b.append(c,s);b.setAttribute('aria-label','Chọn mẫu '+people[i].name);b.onclick=()=>{presetIndex=i;clearPerson();};$('preset-list').append(b);}
async function readFile(file){
  if(!['image/png','image/jpeg','image/webp'].includes(file.type))throw new Error('Chỉ nhận ảnh PNG, JPG hoặc WebP.');
  if(file.size>10*1024*1024)throw new Error('Mỗi ảnh tối đa 10 MiB.');
  const bytes=new Uint8Array(await file.slice(0,12).arrayBuffer());
  const matches=file.type==='image/png'?bytes[0]===137&&bytes[1]===80&&bytes[2]===78&&bytes[3]===71:file.type==='image/jpeg'?bytes[0]===255&&bytes[1]===216:bytes[0]===82&&bytes[1]===73&&bytes[2]===70&&bytes[3]===70&&bytes[8]===87&&bytes[9]===69&&bytes[10]===66&&bytes[11]===80;
  if(!matches)throw new Error('Nội dung ảnh không khớp định dạng.');
  const src=await new Promise((resolve,reject)=>{const reader=new FileReader();reader.onload=()=>resolve(reader.result);reader.onerror=()=>reject(new Error('Không đọc được ảnh.'));reader.readAsDataURL(file);});
  const image=await imageFrom(src);if(image.naturalWidth*image.naturalHeight>16000000)throw new Error('Chọn ảnh dưới 16 triệu pixel.');return{src,image};
}
$('upload-art').onclick=()=>$('art-file').click();
$('art-file').onchange=async e=>{
  const files=[...e.target.files],epoch=session,surface=draft.side;e.target.value='';
  if(draft.assets.length+files.length>5){message('Tối đa 5 hình in trong một thiết kế.',true);return;}
  for(const file of files){try{const{src,image}=await readFile(file);if(epoch!==session)return;if(draft.assets.length>=5)throw new Error('Tối đa 5 hình in.');
    const ratio=image.naturalHeight/image.naturalWidth,w=Math.min(140,300,200/ratio),h=w*ratio;
    const a={id:crypto.randomUUID(),name:file.name,original:src,active:src,image,side:surface,x:(300-w)/2,y:40,w,h};draft.assets.push(a);draft.selected=a.id;changed();message('Đã thêm hình in. Kéo trên áo hoặc nhập vị trí.');
  }catch(err){message(err.message,true);}}
};
for(const[key,id]of[['x','pos-x'],['y','pos-y'],['w','pos-w'],['h','pos-h']]){
  const update=commit=>{
    const a=selected();if(!a)return;let value=Number($(id).value);
    if(!Number.isFinite(value)||$(id).value===''){if(commit){message('Nhập số hợp lệ.',true);$(id).value=Math.round(a[key]);}return;}
    const max=key==='x'?300-a.w:key==='y'?400-a.h:key==='w'?300-a.x:400-a.y;const next=Math.max(key==='w'||key==='h'?1:0,Math.min(max,value));
    a[key]=next;$(id).value=Math.round(next);changed();message(next!==value?'Đã giới hạn hình in trong vùng in.':'Đã cập nhật vị trí.');
  };
  $(id).oninput=()=>update(false);$(id).onchange=()=>update(true);
}
editor.onpointerdown=e=>{const point=pointInPrint(editor,e,draft.side),a=[...draft.assets].reverse().find(a=>a.side===draft.side&&point.x>=a.x&&point.x<=a.x+a.w&&point.y>=a.y&&point.y<=a.y+a.h);if(!a)return;draft.selected=a.id;drag={id:a.id,dx:point.x-a.x,dy:point.y-a.y};editor.setPointerCapture(e.pointerId);render();};
editor.onpointermove=e=>{if(!drag)return;const a=selected();if(!a)return;const point=pointInPrint(editor,e,draft.side);a.x=Math.max(0,Math.min(300-a.w,point.x-drag.dx));a.y=Math.max(0,Math.min(400-a.h,point.y-drag.dy));changed();};
editor.onpointerup=editor.onpointercancel=()=>{drag=null;};
async function api(path,payload,signal){let r;try{r=await fetch(path,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(payload),signal,cache:'no-store'});}catch(err){if(err.name==='AbortError')throw err;throw new Error('Không kết nối được máy chủ. Thiết kế vẫn được giữ trong phiên.');}let data;try{data=await r.json();}catch{throw new Error('Máy chủ không phản hồi. Kiểm tra demo đang chạy.');}if(!r.ok)throw new Error(data.error?.message||'Xử lý thất bại.');return data;}
function closeBackground(){bgToken++;bgController?.abort();review=null;$('background-dialog').close();$('bg-original').removeAttribute('src');$('bg-result').removeAttribute('src');$('run-removal').disabled=false;}
$('remove-bg').onclick=()=>{const a=selected();if(!a)return;bgToken++;review={assetId:a.id,input:a.active,output:null,epoch:session};$('bg-original').src=a.active;$('bg-result').hidden=true;$('bg-result').removeAttribute('src');$('bg-placeholder').hidden=false;$('bg-status').textContent='';$('apply-bg').disabled=true;$('background-dialog').showModal();};
$('close-dialog').onclick=$('cancel-bg').onclick=closeBackground;$('background-dialog').addEventListener('cancel',e=>{e.preventDefault();closeBackground();});
$('bg-mode').onchange=()=>{$('tolerance-wrap').hidden=$('bg-mode').value!=='solid';};
$('run-removal').onclick=async()=>{
  if(!review)return;const token=++bgToken,epoch=session,input=review.input;bgController?.abort();bgController=new AbortController();$('run-removal').disabled=true;$('apply-bg').disabled=true;$('bg-status').textContent=$('bg-mode').value==='subject'?'Đang tách chủ thể… Lần đầu có thể cần tải mô hình.':'Đang xóa nền đơn sắc…';
  try{const data=await api('/api/remove-background',{image:input,mode:$('bg-mode').value,tolerance:Number($('bg-tolerance').value)},bgController.signal);await imageFrom(data.image);if(token!==bgToken||epoch!==session||!review)return;review.output=data.image;$('bg-result').src=data.image;$('bg-result').hidden=false;$('bg-placeholder').hidden=true;$('apply-bg').disabled=false;$('bg-status').textContent='Kiểm tra viền và chi tiết trước khi áp dụng.';}
  catch(err){if(err.name!=='AbortError'&&token===bgToken)$('bg-status').textContent=err.message;}finally{if(token===bgToken)$('run-removal').disabled=false;}
};
$('apply-bg').onclick=async()=>{if(!review?.output)return;const active=review,epoch=session;const img=await imageFrom(active.output);if(epoch!==session||review!==active)return;const a=draft.assets.find(a=>a.id===active.assetId);if(a){a.active=active.output;a.image=img;}closeBackground();changed();message('Đã áp dụng ảnh trong suốt. Vị trí hình in được giữ nguyên.');};
$('restore-art').onclick=async()=>{const a=selected(),epoch=session;if(!a)return;const image=await imageFrom(a.original);if(epoch!==session||!draft.assets.includes(a))return;a.active=a.original;a.image=image;changed();message('Đã khôi phục ảnh gốc.');};
function clearPerson(){personToken++;tryonToken++;requestController?.abort();generating=false;person=null;result=null;showOriginal=false;$('generation-overlay').hidden=true;$('person-file').value='';render();}
$('upload-person').onclick=()=>$('person-file').click();$('clear-person').onclick=clearPerson;
$('person-file').onchange=async e=>{const file=e.target.files[0],epoch=session;e.target.value='';if(!file)return;const token=++personToken;tryonToken++;try{const input=await readFile(file);if(epoch!==session||token!==personToken)return;requestController?.abort();generating=false;$('generation-overlay').hidden=true;person=input;result=null;showOriginal=false;render();message('Đã chọn ảnh. Bấm Thử áo trên tôi để AI thay áo.');}catch(err){if(epoch===session)message(err.message,true);}};
$('external-consent').onchange=render;$('show-original').onclick=()=>{showOriginal=!showOriginal;render();};
async function refreshEngine(){const response=await fetch('/api/status',{cache:'no-store'});if(!response.ok)throw new Error('Không kiểm tra được AI.');engine=(await response.json()).tryOn;$('engine-note').textContent=engine.notice;$('external-consent-wrap').hidden=engine.engine!=='openai';render();}
$('generate').onclick=async()=>{
  if(!person||generating)return;const epoch=session,token=personToken,revision=draft.revision,jobToken=++tryonToken;
  const captured={session:epoch,person:token,revision,job:jobToken};
  const current=()=>({session,person:personToken,revision:draft.revision,job:tryonToken});
  try{await refreshEngine();}catch{message('Không kết nối được máy chủ demo.',true);return;}
  if(!acceptsTryOn(captured,current(),revision))return;
  if(!engine?.available){message(engine?.notice||'AI chưa sẵn sàng.',true);return;}
  requestController=new AbortController();generating=true;$('generation-overlay').hidden=false;render();message('AI đang xử lý ảnh thật. Giữ tab mở để nhận kết quả.');
  try{const data=await api('/api/try-on',{personImage:person.src,garmentImage:garmentImage(draft),designRevision:revision,externalConsent:$('external-consent').checked},requestController.signal);await imageFrom(data.image);if(!acceptsTryOn(captured,current(),data.designRevision))return;result=data;showOriginal=false;message('Đã tạo ảnh thử áo. Hãy kiểm tra lại logo và chi tiết.');}
  catch(err){if(err.name!=='AbortError'&&epoch===session&&token===personToken&&jobToken===tryonToken)message(err.message,true);}
  finally{if(epoch===session&&token===personToken&&jobToken===tryonToken){generating=false;$('generation-overlay').hidden=true;render();}}
};
function dispose(){session++;personToken++;bgToken++;tryonToken++;requestController?.abort();bgController?.abort();draft.assets=[];draft.selected=null;person=null;result=null;review=null;generating=false;drag=null;$('person-thumbnail').removeAttribute('src');$('personal-result').removeAttribute('src');$('bg-original').removeAttribute('src');$('bg-result').removeAttribute('src');$('art-file').value='';$('person-file').value='';$('external-consent').checked=false;$('asset-list').replaceChildren();document.querySelectorAll('canvas').forEach(c=>c.getContext('2d').clearRect(0,0,c.width,c.height));}
$('end-session').onclick=()=>{dispose();draft={colour:palette[0][1],fabric:'cotton',side:'front',revision:0,assets:[],selected:null};if($('background-dialog').open)$('background-dialog').close();$('generation-overlay').hidden=true;switchTab('design');message('Đã kết thúc phiên và bỏ toàn bộ ảnh. Bạn có thể bắt đầu thiết kế mới.');};
window.addEventListener('pagehide',dispose);window.addEventListener('pageshow',e=>{if(e.persisted)location.reload();});
try{
  await loadTemplates();templatesReady=true;
  if(session===0&&draft.assets.length===0){const src=sampleArtwork(),image=await imageFrom(src);if(session===0&&draft.assets.length===0){draft.assets=[{id:crypto.randomUUID(),name:'Weave · mẫu minh họa',original:src,active:src,image,side:'front',x:95,y:35,w:110,h:110}];draft.selected=draft.assets[0].id;}}
  render();
  await refreshEngine();
}catch(err){message(err.message,true);$('engine-note').textContent='Không kết nối được máy chủ demo.';}
