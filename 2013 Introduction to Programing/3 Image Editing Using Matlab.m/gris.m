function [ r ] = gris (x)
%Su función debe recibir como parámetro la matriz correspondiente a 
%una imagen cualquiera, y debe devolver la matriz correspondiente a 
%la misma imagen pero en escala de grises.
rojo = x(:,:,1);
verde= x(:,:,2);
azul= x(:,:,3);
r= rojo*0.299+verde*0.587+azul*0.114;


end

