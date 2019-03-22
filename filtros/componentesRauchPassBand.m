q=4.52;
qo=1.5;

wo=111753;
R1=82e3;
C1=444e-12;
C2=444e-12;


alpha=(qo-q)/(-2*q*qo^2);
k=alpha/(1+alpha);

r=1/(3*C1*wo);
a=r/R1;
R2=9*r;
R3=r/(1-a);
r6=k*r;
r7=(1-k)*r;

wob=141306;
R1b=47e3;
C1b=680e-12;
C2b=680e-12;

alphab=(qo-q)/(-2*q*qo^2);
kb=alphab/(1+alphab);

rb=1/(3*C1b*wob);
ab=rb/R1b;
R2b=9*rb;
R3b=rb/(1-ab);
r6b=kb*rb;
r7b=(1-kb)*rb;