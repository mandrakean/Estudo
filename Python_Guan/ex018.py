from math import radians, cos, sin, tan
base = float(input('digite um ângulo: '))
sen = sin(radians(base))
cos = cos(radians(base))
tan = tan(radians(base))
print('para o ângulo {}º, o seno é {:.2f}, o coseno é {:.2f} e a tangente é {:.2f}'.format(base, sen, cos, tan))
