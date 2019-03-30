clearvars
clc

% Q = 2.33
wo = 2*pi*4533.04;
Q = 2.33;
C = 1e-9;
k = 3 - 1/Q(length(Q));
R = 1/(wo(length(wo))*C(length(C)));

%Q = 1.18
wo = [wo 2*pi*3604.1];
Q = [Q 1.18];
C = [C 1e-9];
k = [k 3-1/Q(length(Q))];
R = [R 1/(wo(length(wo))*C(length(C)))];

%Q = 0.68
wo = [wo 2*pi*2568.44];
Q = [Q 0.68];
C = [C 1e-9];
k = [k 3-1/Q(length(Q))];
R = [R 1/(wo(length(wo))*C(length(C)))]

%Q = 0.5
% wo = [wo 2*pi*2008.98]
% Q = [Q 0.5]
% C = [C 1e-9]
% k = [k 3-1/Q(length(Q))]
% R = [R 1/(wo(length(wo))*C(length(C)))]

