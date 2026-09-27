// Bilinear sampling in premultiplied alpha avoids dark cutout edges.
export function samplePrint(data,width,height,x,y){
  x=Math.max(0,Math.min(width-1,x));y=Math.max(0,Math.min(height-1,y));
  const x0=Math.floor(x),y0=Math.floor(y),fx=x-x0,fy=y-y0;
  let alpha=0,r=0,g=0,b=0;
  for(const [dx,dy,weight] of [[0,0,(1-fx)*(1-fy)],[1,0,fx*(1-fy)],[0,1,(1-fx)*fy],[1,1,fx*fy]]){
    const p=(Math.min(height-1,y0+dy)*width+Math.min(width-1,x0+dx))*4,a=data[p+3]*weight;
    alpha+=a;r+=data[p]*a;g+=data[p+1]*a;b+=data[p+2]*a;
  }
  return alpha?[r/alpha,g/alpha,b/alpha,alpha]:[0,0,0,0];
}

// Each destination pixel is assigned, never composited twice across mesh seams.
export function rasterPrint(source,sw,sh,width,height,triangles){
  const out=new Uint8ClampedArray(width*height*4);
  for(const {source:s,target:t} of triangles){
    const [a,b,c]=t,den=(b[1]-c[1])*(a[0]-c[0])+(c[0]-b[0])*(a[1]-c[1]);
    if(Math.abs(den)<1e-8)continue;
    const minX=Math.max(0,Math.floor(Math.min(...t.map(p=>p[0])))),maxX=Math.min(width-1,Math.ceil(Math.max(...t.map(p=>p[0]))));
    const minY=Math.max(0,Math.floor(Math.min(...t.map(p=>p[1])))),maxY=Math.min(height-1,Math.ceil(Math.max(...t.map(p=>p[1]))));
    for(let y=minY;y<=maxY;y++)for(let x=minX;x<=maxX;x++){
      const px=x+.5,py=y+.5;
      const u=((b[1]-c[1])*(px-c[0])+(c[0]-b[0])*(py-c[1]))/den;
      const v=((c[1]-a[1])*(px-c[0])+(a[0]-c[0])*(py-c[1]))/den,w=1-u-v;
      if(u< -1e-7||v< -1e-7||w< -1e-7)continue;
      const sample=samplePrint(source,sw,sh,u*s[0][0]+v*s[1][0]+w*s[2][0]-.5,u*s[0][1]+v*s[1][1]+w*s[2][1]-.5);
      out.set(sample,(y*width+x)*4);
    }
  }
  return out;
}

// Opaque ink retains its own colour; fabric contributes light and fine texture.
export function inkLight(luminance,localMean){
  const shape=Math.max(.6,Math.min(1.08,luminance/235));
  const texture=Math.max(.85,Math.min(1.12,luminance/Math.max(1,localMean)));
  return Math.max(.5,Math.min(1.12,Math.pow(shape,1.35)*texture));
}
