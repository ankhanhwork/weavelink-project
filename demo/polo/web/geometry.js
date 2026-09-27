// Physical print coordinates project through the same calibrated garment plane.
export function corners(area){
  if(area.quad)return area.quad;
  const [x,y]=area.origin,[ux,uy]=area.u,[vx,vy]=area.v;
  return [[x,y],[x+ux,y+uy],[x+ux+vx,y+uy+vy],[x+vx,y+vy]];
}
export function homography(area){
  const [[x0,y0],[x1,y1],[x2,y2],[x3,y3]]=corners(area);
  const dx1=x1-x2,dx2=x3-x2,dy1=y1-y2,dy2=y3-y2;
  const sx=x0-x1+x2-x3,sy=y0-y1+y2-y3,den=dx1*dy2-dx2*dy1;
  const g=(sx*dy2-dx2*sy)/den,h=(dx1*sy-sx*dy1)/den;
  return [x1-x0+g*x1,x3-x0+h*x3,x0,y1-y0+g*y1,y3-y0+h*y3,y0,g,h,1];
}
export function project(matrix,x,y){
  const [a,b,c,d,e,f,g,h,i]=matrix,z=g*x+h*y+i;
  return [(a*x+b*y+c)/z,(d*x+e*y+f)/z];
}
export function inverse(m){
  const [a,b,c,d,e,f,g,h,i]=m;
  const out=[e*i-f*h,c*h-b*i,b*f-c*e,f*g-d*i,a*i-c*g,c*d-a*f,d*h-e*g,b*g-a*h,a*e-b*d];
  const det=a*out[0]+b*out[3]+c*out[6];return out.map(v=>v/det);
}
export function chestPlacement(kind,ratio=1){
  const w=Math.min(70,90/ratio),h=w*ratio;
  return {x:kind==='left'?240-w/2:60-w/2,y:18,w,h};
}

// Independent garment landmarks, not subdivisions of a single flat projection.
export function surfacePoint(area,u,v){
  if(!area.surface)return project(homography(area),u,v);
  const grid=area.surface,rows=grid.length-1,cols=grid[0].length-1;
  const x=Math.max(0,Math.min(cols,u*cols)),y=Math.max(0,Math.min(rows,v*rows));
  const i=Math.min(cols-1,Math.floor(x)),j=Math.min(rows-1,Math.floor(y));
  const s=x-i,t=y-j;
  return [0,1].map(k=>(1-t)*((1-s)*grid[j][i][k]+s*grid[j][i+1][k])+t*((1-s)*grid[j+1][i][k]+s*grid[j+1][i+1][k]));
}
