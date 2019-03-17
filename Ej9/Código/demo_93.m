clearvars
clc
syms w T
y = atan((2*sin(w*T) + 3*sin(w*T*2) + 4*sin(3*w*T) +3*sin(w*T*4) + 2*sin(w*T*5) + sin(w*T*6)) / (1+ 2*cos(w*T) + 3*cos(2*w*T) + 4* cos(3*w*T) + 3*cos(4*w*T) + 2*cos(5*w*T) + cos(6*w*T)));
%pretty(diff(y,w))
diffy = simplify(diff(y,w))

