// Photographic templates are synthetic; current artwork is rendered deterministically.
import {homography,project,inverse,surfacePoint} from './geometry.js';
import {rasterPrint,inkLight} from './print-surface.js';
export const views = [
  {name:'Trước · Flat lay', side:'front', tile:0, origin:[.255,.235], u:[.49,0], v:[0,.65]},
  {name:'Trước · Dáng áo', side:'front', tile:1, origin:[.29,.23], u:[.42,0], v:[0,.67]},
  {name:'Nghiêng trái', side:'front', tile:2, quad:[[.25,.245],[.57,.29],[.69,.91],[.31,.88]]},
  {name:'Nghiêng phải', side:'front', tile:3, quad:[[.405,.285],[.735,.245],[.685,.88],[.30,.91]]},
  {name:'Sau · Flat lay', side:'back', tile:4, origin:[.29,.28], u:[.42,0], v:[0,.56]},
  {name:'Sau · Dáng áo', side:'back', tile:5, origin:[.30,.28], u:[.40,0], v:[0,.56]},
];
// Rows span the chest to hem; the centre column follows the button placket.
views[2].surface=[
  [[.225,.245],[.30,.25],[.40,.25],[.535,.25],[.665,.255]],
  [[.245,.393],[.288375,.400],[.388375,.405],[.518375,.412],[.67,.402]],
  [[.255,.552],[.304375,.560],[.409375,.565],[.527375,.572],[.67,.56]],
  [[.26,.714],[.314375,.722],[.429375,.725],[.539375,.73],[.675,.719]],
  [[.267,.876],[.326375,.882],[.446375,.885],[.550375,.886],[.68,.877]]
];
views[3].surface=[
  [[.30,.25],[.425,.25],[.568,.25],[.645,.245],[.724,.235]],
  [[.305,.412],[.45853125,.412],[.59053125,.41],[.67053125,.40],[.71,.39]],
  [[.31,.577],[.46253125,.577],[.57453125,.572],[.65953125,.565],[.704,.555]],
  [[.305,.736],[.45753125,.736],[.55653125,.73],[.64253125,.722],[.693,.715]],
  [[.30,.892],[.44453125,.892],[.53253125,.886],[.62253125,.88],[.68,.872]]
];
views[2].occlusion=[[.395,.21],[.422,.21],[.42,.348],[.387,.348]];
views[3].occlusion=[[.547,.225],[.578,.22],[.60,.325],[.56,.329]];
export const people = [
  {name:'Nam', area:{origin:[.26,.43],u:[.48,0],v:[0,.31]}, mask:[[.37,.24],[.63,.24],[.73,.27],[.88,.32],[.95,.48],[.79,.50],[.82,.77],[.20,.77],[.22,.50],[.05,.49],[.12,.34],[.28,.28]]},
  {name:'Nữ', area:{origin:[.28,.43],u:[.43,0],v:[0,.29]}, mask:[[.39,.25],[.59,.25],[.74,.29],[.83,.34],[.91,.45],[.77,.49],[.78,.74],[.24,.74],[.24,.48],[.10,.46],[.18,.33],[.29,.29]]},
  {name:'Trẻ em', area:{origin:[.335,.525],u:[.33,0],v:[0,.22]}, mask:[[.39,.37],[.64,.37],[.78,.41],[.89,.45],[.94,.54],[.82,.56],[.81,.77],[.25,.77],[.27,.55],[.12,.54],[.21,.43],[.30,.40]]},
];
let poloSheet, peopleSheet;
const baseCache = new Map();
const lightCache = new Map();
function fabricLight(index){
  if(!lightCache.has(index))lightCache.set(index,base('polo',index,'#eee9dc').getContext('2d').getImageData(0,0,512,512).data);
  return lightCache.get(index);
}
function foldPoint(area,p){
  if(!area.surface)return p;
  const data=fabricLight(area.tile),x=Math.round(p[0]*511),y=Math.round(p[1]*511);
  const light=(dx,dy)=>{const q=(Math.max(0,Math.min(511,y+dy))*512+Math.max(0,Math.min(511,x+dx)))*4;return (data[q]+data[q+1]+data[q+2])/3;};
  const limit=v=>Math.max(-.003,Math.min(.003,v));
  return [p[0]+limit((light(-4,0)-light(4,0))*.00012),p[1]+limit((light(0,-4)-light(0,4))*.00012)];
}
export function imageFrom(src) { return new Promise((resolve,reject)=>{const img=new Image();img.onload=()=>resolve(img);img.onerror=()=>reject(new Error('Không đọc được ảnh.'));img.src=src;}); }
export async function loadTemplates(){[poloSheet,peopleSheet]=await Promise.all([imageFrom('/assets/polo-views.png'),imageFrom('/assets/people.png')]);}
function rgb(hex){return [1,3,5].map(i=>parseInt(hex.slice(i,i+2),16));}
function base(kind,index,colour){
  const key=`${kind}-${index}-${colour}`; if(baseCache.has(key))return baseCache.get(key);
  const canvas=document.createElement('canvas');const c=canvas.getContext('2d',{willReadFrequently:true});
  canvas.width=512;canvas.height=kind==='polo'?512:1024;
  const source=kind==='polo'?poloSheet:peopleSheet;
  const sw=source.width/3,sh=kind==='polo'?source.height/2:source.height;
  c.drawImage(source,(index%3)*sw,kind==='polo'?Math.floor(index/3)*sh:0,sw,sh,0,0,canvas.width,canvas.height);
  if(colour!=='#eee9dc'){
    let mask;
    if(kind==='person'){
      const m=document.createElement('canvas');m.width=512;m.height=1024;const mc=m.getContext('2d');
      mc.beginPath();people[index].mask.forEach(([x,y],i)=>i?mc.lineTo(x*512,y*1024):mc.moveTo(x*512,y*1024));mc.closePath();mc.fill();mask=mc.getImageData(0,0,512,1024).data;
    }
    const pixels=c.getImageData(0,0,canvas.width,canvas.height),d=pixels.data, target=rgb(colour);
    for(let p=0;p<d.length;p+=4){
      const r=d[p],g=d[p+1],b=d[p+2];
      const cloth=r>120&&g>115&&b>100&&r-b>3&&r-b<40&&Math.abs(r-g)<18&&g-b<28;
      if(cloth&&(!mask||mask[p+3])){
        const shade=Math.min(1.13,(r+g+b)/3/235);
        const blend=Math.min(1,(r-b-3)/5);
        for(let ch=0;ch<3;ch++)d[p+ch]=Math.min(255,target[ch]*shade)*blend+d[p+ch]*(1-blend);
      }
    }
    c.putImageData(pixels,0,0);
  }
  baseCache.set(key,canvas);return canvas;
}
function drawArt(ctx,assets,area,side,w,h){
  if(area.surface||area.quad){
    const plane=document.createElement('canvas');plane.width=600;plane.height=800;
    const pc=plane.getContext('2d');for(const a of assets.filter(a=>a.side===side))pc.drawImage(a.image,a.x*2,a.y*2,a.w*2,a.h*2);
    const cols=12,rows=16,triangles=[];
    const point=(x,y)=>{const p=foldPoint(area,surfacePoint(area,x/cols,y/rows));return [p[0]*w,p[1]*h];};
    for(let y=0;y<rows;y++)for(let x=0;x<cols;x++){
      const source=[[x*600/cols,y*800/rows],[(x+1)*600/cols,y*800/rows],[(x+1)*600/cols,(y+1)*800/rows],[x*600/cols,(y+1)*800/rows]];
      const target=[point(x,y),point(x+1,y),point(x+1,y+1),point(x,y+1)];
      for(const ids of [[0,1,2],[0,2,3]])triangles.push({source:ids.map(i=>source[i]),target:ids.map(i=>target[i])});
    }
    const warped=document.createElement('canvas');warped.width=w;warped.height=h;
    const wc=warped.getContext('2d'),pixels=wc.createImageData(w,h);
    pixels.data.set(rasterPrint(pc.getImageData(0,0,600,800).data,600,800,w,h,triangles));
    wc.putImageData(pixels,0,0);ctx.drawImage(warped,0,0);return;
  }
  ctx.save();const {origin:o,u,v}=area;
  ctx.transform(u[0]*w,u[1]*h,v[0]*w,v[1]*h,o[0]*w,o[1]*h);
  ctx.beginPath();ctx.rect(0,0,1,1);ctx.clip();
  for(const a of assets.filter(a=>a.side===side))ctx.drawImage(a.image,a.x/300,a.y/400,a.w/300,a.h/400);
  ctx.restore();
}
export function renderPolo(canvas,draft,viewIndex=0,editor=false){
  const ctx=canvas.getContext('2d'),w=canvas.width,h=canvas.height,view=views[viewIndex];
  ctx.clearRect(0,0,w,h);ctx.fillStyle='white';ctx.fillRect(0,0,w,h);ctx.drawImage(base('polo',view.tile,draft.colour),0,0,w,h);
  if(!editor){
    const overlay=document.createElement('canvas');overlay.width=w;overlay.height=h;
    const oc=overlay.getContext('2d',{willReadFrequently:true});
    drawArt(oc,draft.assets,view,view.side,w,h);
    // Retain artwork alpha while transferring the blank garment's light/texture.
    const art=oc.getImageData(0,0,w,h),shade=fabricLight(view.tile);
    for(let y=0;y<h;y++)for(let x=0;x<w;x++){
      const p=(y*w+x)*4;if(!art.data[p+3])continue;
      const q=(Math.min(511,Math.floor(y*512/h))*512+Math.min(511,Math.floor(x*512/w)))*4;
      let mean=0;
      const sx=Math.min(511,Math.floor(x*512/w)),sy=Math.min(511,Math.floor(y*512/h));
      for(const [dx,dy]of [[-3,0],[3,0],[0,-3],[0,3]]){
        const n=(Math.max(0,Math.min(511,sy+dy))*512+Math.max(0,Math.min(511,sx+dx)))*4;
        mean+=(shade[n]+shade[n+1]+shade[n+2])/12;
      }
      const light=inkLight((shade[q]+shade[q+1]+shade[q+2])/3,mean);
      for(let k=0;k<3;k++)art.data[p+k]*=light;
    }
    oc.putImageData(art,0,0);
    if(view.occlusion){oc.globalCompositeOperation='destination-out';oc.beginPath();view.occlusion.forEach(([x,y],i)=>i?oc.lineTo(x*w,y*h):oc.moveTo(x*w,y*h));oc.closePath();oc.fill();}
    ctx.drawImage(overlay,0,0);
  }else drawArt(ctx,draft.assets,view,view.side,w,h);
  if(editor){
    const {origin:o,u,v}=view;ctx.save();ctx.transform(u[0]*w,u[1]*h,v[0]*w,v[1]*h,o[0]*w,o[1]*h);
    ctx.lineWidth=.002;ctx.strokeStyle='#829678';ctx.setLineDash([.012,.009]);ctx.strokeRect(0,0,1,1);
    const a=draft.assets.find(a=>a.id===draft.selected&&a.side===draft.side);
    if(a){ctx.setLineDash([]);ctx.strokeStyle='#637d43';ctx.lineWidth=.004;ctx.strokeRect(a.x/300,a.y/400,a.w/300,a.h/400);
      ctx.fillStyle='#637d43';for(const [x,y]of[[a.x/300,a.y/400],[(a.x+a.w)/300,a.y/400],[a.x/300,(a.y+a.h)/400],[(a.x+a.w)/300,(a.y+a.h)/400]])ctx.fillRect(x-.007,y-.007,.014,.014);
    }ctx.restore();
  }
}
export function renderPerson(canvas,draft,index=0){
  const ctx=canvas.getContext('2d'),w=canvas.width,h=canvas.height;
  ctx.clearRect(0,0,w,h);ctx.drawImage(base('person',index,draft.colour),0,0,w,h);
  drawArt(ctx,draft.assets,people[index].area,'front',w,h);
}
export function garmentImage(draft){const c=document.createElement('canvas');c.width=768;c.height=768;renderPolo(c,draft,0);return c.toDataURL('image/png');}
export function sampleArtwork(){
  const c=document.createElement('canvas');c.width=480;c.height=480;const ctx=c.getContext('2d');
  ctx.fillStyle='#ffffff';ctx.fillRect(0,0,480,480);
  ctx.translate(240,207);for(let i=0;i<8;i++){ctx.save();ctx.rotate(i*Math.PI/4);ctx.fillStyle=i%2?'#d2de9b':'#afc2ba';ctx.beginPath();ctx.ellipse(0,-62,24,68,0,0,Math.PI*2);ctx.fill();ctx.restore();}
  ctx.fillStyle='#d69a62';ctx.beginPath();ctx.arc(0,0,38,0,Math.PI*2);ctx.fill();ctx.setTransform(1,0,0,1,0,0);
  ctx.textAlign='center';ctx.fillStyle='#203e34';ctx.font='bold 46px Georgia';ctx.fillText('WEAVE',240,387);ctx.font='14px sans-serif';ctx.fillText('G R O W   Y O U R   W A Y',240,425);
  return c.toDataURL('image/png');
}
export function pointInPrint(canvas,event,side){
  const r=canvas.getBoundingClientRect(),v=views[side==='front'?0:4];
  const p=project(inverse(homography(v)),(event.clientX-r.left)/r.width,(event.clientY-r.top)/r.height);
  return{x:p[0]*300,y:p[1]*400};
}
