import test from 'node:test';
import assert from 'node:assert/strict';
import {homography,project,inverse,corners,chestPlacement,surfacePoint} from '../web/geometry.js';
import {views} from '../web/render.js';
const near=(a,b)=>assert.ok(Math.abs(a-b)<1e-9,`${a} != ${b}`);
for(const view of views){
  test(`${view.name}: physical corners and drag round trip`,()=>{
    const m=homography(view),back=inverse(m),quad=corners(view);
    [[0,0],[1,0],[1,1],[0,1]].forEach(([x,y],i)=>project(m,x,y).forEach((v,j)=>near(v,quad[i][j])));
    for(const [x,y] of [[0,0],[.8,.13],[.2,.13],[.5,.5],[1,1]]){
      const p=project(m,x,y),restored=project(back,...p);near(restored[0],x);near(restored[1],y);
    }
  });
}
test('wearer left/right chest are mirrored, bounded and above centre print',()=>{
  const left=chestPlacement('left',1.5),right=chestPlacement('right',1.5);
  near(left.x+left.w/2+right.x+right.w/2,300);
  for(const a of [left,right]){assert.ok(a.x>=0&&a.x+a.w<=300);assert.ok(a.y+a.h<120);assert.ok(a.w<=70);near(a.h/a.w,1.5);}
  assert.equal(chestPlacement('left',1).w,70);
});

test('centred proof uses the authored centre column without rejected extra offsets',()=>{
  for(const view of views){assert.equal(view.registration,undefined);}
  for(const view of [views[2],views[3]])for(let j=0;j<5;j++){
    assert.deepEqual(surfacePoint(view,.5,j/4),view.surface[j][2]);
  }
});
test('angle proof mesh remains continuous and never folds cells',()=>{
  for(const view of [views[2],views[3]])for(let j=0;j<16;j++)for(let i=0;i<12;i++){
    const a=surfacePoint(view,i/12,j/16),b=surfacePoint(view,(i+1)/12,j/16),c=surfacePoint(view,(i+1)/12,(j+1)/16),d=surfacePoint(view,i/12,(j+1)/16);
    const cross=(p,q,r)=>(q[0]-p[0])*(r[1]-p[1])-(q[1]-p[1])*(r[0]-p[0]);
    assert.ok(cross(a,b,c)>0&&cross(a,c,d)>0);
  }
});

for(const view of views.filter(v=>v.surface))test(`${view.name}: surface landmarks, chest sides and non-folding cells`,()=>{
  view.surface.forEach((row,j)=>row.forEach((p,i)=>surfacePoint(view,i/4,j/4).forEach((v,k)=>near(v,p[k]))));
  for(let j=0;j<4;j++)for(let i=0;i<4;i++){
    const a=surfacePoint(view,i/4,j/4),b=surfacePoint(view,(i+1)/4,j/4),c=surfacePoint(view,(i+1)/4,(j+1)/4),d=surfacePoint(view,i/4,(j+1)/4);
    const cross=(p,q,r)=>(q[0]-p[0])*(r[1]-p[1])-(q[1]-p[1])*(r[0]-p[0]);
    assert.ok(cross(a,b,c)>0&&cross(a,c,d)>0,'surface cell folds over');
  }
  const l=surfacePoint(view,.8,.13),r=surfacePoint(view,.2,.13),centre=surfacePoint(view,.5,.13);
  assert.ok(r[0]<centre[0]&&centre[0]<l[0]);
  const lowerLogoV=(214+35)/400,front=surfacePoint(views[0],.5,lowerLogoV),angled=surfacePoint(view,.5,lowerLogoV);
  assert.ok(Math.abs(angled[1]-front[1])<.02,'lower torso logo must not drift vertically between views');
});
