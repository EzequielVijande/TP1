% clearvars
% clc
% 
% m_limit = 10
% fo = 1e3;
% fos = (1:m_limit) * fo;
% xo = 1/(12*fo^3);
% relacion = []
% 
% syms k
% for m = 1:m_limit
% 	S_symsum = xo^2 + 2*symsum(1/k^4, k, 1, m);
% 	relacion = [relacion S_symsum/(pi^4/45 + xo^2)];
% end 
% 
% plot(fos, relacion);

clearvars
clc

m_limit = 10
fo = 1e3;
fos = (1:m_limit) * 2/3*fo;
relacion = []

syms k
for m = 1:m_limit
	S_symsum = symsum(1/(4*k^2-9)^2, k, -m, m);
	relacion = [relacion S_symsum/(pi^2/72)];
end 

plot(fos, relacion);

