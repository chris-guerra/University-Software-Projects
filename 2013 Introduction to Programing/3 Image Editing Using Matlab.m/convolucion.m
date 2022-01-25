function [O] = convolucion(I,K)
[M,N]=size(I);
[m,n]=size(K);
a=M-m+1;
b=N-n+1;
matriz=zeros(a,b);
for filamatriz = 1:a
    for columnamatriz = 1:b
        for fmatriz = 1:m
            for cmatriz = 1:n
                p=fmatriz+filamatriz-1;
                q=cmatriz+columnamatriz-1;
                y=I(p,q);
                z=K(fmatriz,cmatriz);
                matriz(filamatriz,columnamatriz)= matriz(filamatriz,columnamatriz)+(y*z);
            end
        end
    end
end
                
O=matriz;

end

