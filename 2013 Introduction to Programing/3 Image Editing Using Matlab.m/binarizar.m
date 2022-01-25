function [r] = binarizar(x,cota)
[m,n]=size(x);
final=ones(m,n);
for fila = 1:m
    for columna = 1:n
        a=x(fila,columna);
        if a<cota
            final(fila,columna)=0;
        else
            final(fila,columna)=255;
        end
    end
end     
r=final;
end