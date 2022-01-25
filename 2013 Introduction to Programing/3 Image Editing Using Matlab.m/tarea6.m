narchivo=input('Imagen?');
nsalida=input('Archivo de salida?');
imagen= imread (narchivo);
gray= gris(imagen);
gray= double(gray);

M1=[1 0; 0 -1];
M2=[0 1; -1 0];
C1=convolucion(gray,M1);
C2=convolucion(gray,M2);
[m,n]=size(C1);
D1=C1.^2;
D2=C2.^2;
G=zeros(m,n);

for fila3 = 1:m
    for columna3 = 1:n
        a=D1(fila3,columna3);
        b=D2(fila3,columna3);
        c=(a+b)^(1/2);
        G(fila3,columna3)=c;
    end
end
g2=G;
binarize=binarizar(g2,30);
invert=invertir(binarize);
imwrite (invert, nsalida);