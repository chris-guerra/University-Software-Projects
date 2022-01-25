function [r] = invertir(x)
r=x;
r(r==0)=2;
r(r==255)=0;
r(r==2)=255;


end

