%coeficientes de fourier de t^2 entre -2*tau y 2*tau

clearvars 
clc

syms t
syms n integer
syms tau

% xn = simplify(int(t^2* exp(-pi/2*n*t/tau*i),-2*tau, 2*tau));
% pretty(xn)
% tau = 1
% n = 1:60;
% x = abs((32*(-1).^n*tau^3)./(n.^2*pi^2)).^2
% plot(n,x)

%coeficientes de fourier de sin(2*pi*fo*t) en [0, 3/(2*fo)]

syms fo

yn = simplify(int(sin(2*pi*fo*t) * exp(-i*2*pi*2/3*fo*n*t), 0, 3/(2*fo)))
pretty(yn)
% fo = 1
% n = 1:60;
% % y = -18./(fo*pi*(4*n.^2 - 9))
% y = abs(-18./(fo*pi*(4*n.^2 - 9))).^2
% plot(n,y)
