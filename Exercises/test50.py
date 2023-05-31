#import math # burada import anahtar sözcüğü ile math modlü programın içine dahil ediliyor.

# print(dir(math)) #burada math modülü içerisindeki fonksiyonlara erişmek için dir fonksiyonunu kullanarak erişebiliyoruz

# help(math) # burada math moblü içersinde yer alan fonksiyonların ne işe yaradığını naıl çalıştığını anlamak
# için kullanıldı.

# çıktı => print fonksiyonu çalıştırıldığında elde math modülü içerisinde yer alan fonksiyonlar yazdırıldı. burada
# sadece fonksiyon isimleri görünüyor ama tam olarak ne iş yaptığı ile ilgili bir bilgi yok.

# ['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2',
# 'atanh', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs',
# 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf',
# 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm',
# 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc', 'ulp']


# çıktı => burada help(math) kodu çalıştırıldığında math modülü içerisinde yer alan bütün fonksiyonların adı ve
# açıklaması ekrana yazdırılır. Bu fonksiyonlar ne işe yara nasıl çalıştığı hakkında bilgileri yazdırır. math ifadesini
# yazıp yanına . (nokta) koyunca bu modül ile hangi fonskiyonları kullanabileceğimizi otomatik olarak bize gösterir

# Help on built-in module math:
#
# NAME
#     math
#
# DESCRIPTION
#     This module provides access to the mathematical functions
#     defined by the C standard.
#
# FUNCTIONS
#     acos(x, /)
#         Return the arc cosine (measured in radians) of x.
#
#         The result is between 0 and pi.
#
#     acosh(x, /)
#         Return the inverse hyperbolic cosine of x.
#
#     asin(x, /)
#         Return the arc sine (measured in radians) of x.
#
#         The result is between -pi/2 and pi/2.
#
#     asinh(x, /)
#         Return the inverse hyperbolic sine of x.
#
#     atan(x, /)
#         Return the arc tangent (measured in radians) of x.
#
#         The result is between -pi/2 and pi/2.
#
#     atan2(y, x, /)
#         Return the arc tangent (measured in radians) of y/x.
#
#         Unlike atan(y/x), the signs of both x and y are considered.
#
#     atanh(x, /)
#         Return the inverse hyperbolic tangent of x.
#
#     ceil(x, /)
#         Return the ceiling of x as an Integral.
#
#         This is the smallest integer >= x.
#
#     comb(n, k, /)
#         Number of ways to choose k items from n items without repetition and without order.
#
#         Evaluates to n! / (k! * (n - k)!) when k <= n and evaluates
#         to zero when k > n.
#
#         Also called the binomial coefficient because it is equivalent
#         to the coefficient of k-th term in polynomial expansion of the
#         expression (1 + x)**n.
#
#         Raises TypeError if either of the arguments are not integers.
#         Raises ValueError if either of the arguments are negative.
#
#     copysign(x, y, /)
#         Return a float with the magnitude (absolute value) of x but the sign of y.
#
#         On platforms that support signed zeros, copysign(1.0, -0.0)
#         returns -1.0.
#
#     cos(x, /)
#         Return the cosine of x (measured in radians).
#
#     cosh(x, /)
#         Return the hyperbolic cosine of x.
#
#     degrees(x, /)
#         Convert angle x from radians to degrees.
#
#     dist(p, q, /)
#         Return the Euclidean distance between two points p and q.
#
#         The points should be specified as sequences (or iterables) of
#         coordinates.  Both inputs must have the same dimension.
#
#         Roughly equivalent to:
#             sqrt(sum((px - qx) ** 2.0 for px, qx in zip(p, q)))
#
#     erf(x, /)
#         Error function at x.
#
#     erfc(x, /)
#         Complementary error function at x.
#
#     exp(x, /)
#         Return e raised to the power of x.
#
#     expm1(x, /)
#         Return exp(x)-1.
#
#         This function avoids the loss of precision involved in the direct evaluation of exp(x)-1 for small x.
#
#     fabs(x, /)
#         Return the absolute value of the float x.
#
#     factorial(x, /)
#         Find x!.
#
#         Raise a ValueError if x is negative or non-integral.
#
#     floor(x, /)
#         Return the floor of x as an Integral.
#
#         This is the largest integer <= x.
#
#     fmod(x, y, /)
#         Return fmod(x, y), according to platform C.
#
#         x % y may differ.
#
#     frexp(x, /)
#         Return the mantissa and exponent of x, as pair (m, e).
#
#         m is a float and e is an int, such that x = m * 2.**e.
#         If x is 0, m and e are both 0.  Else 0.5 <= abs(m) < 1.0.
#
#     fsum(seq, /)
#         Return an accurate floating point sum of values in the iterable seq.
#
#         Assumes IEEE-754 floating point arithmetic.
#
#     gamma(x, /)
#         Gamma function at x.
#
#     gcd(*integers)
#         Greatest Common Divisor.
#
#     hypot(...)
#         hypot(*coordinates) -> value
#
#         Multidimensional Euclidean distance from the origin to a point.
#
#         Roughly equivalent to:
#             sqrt(sum(x**2 for x in coordinates))
#
#         For a two dimensional point (x, y), gives the hypotenuse
#         using the Pythagorean theorem:  sqrt(x*x + y*y).
#
#         For example, the hypotenuse of a 3/4/5 right triangle is:
#
#             >>> hypot(3.0, 4.0)
#             5.0
#
#     isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0)
#         Determine whether two floating point numbers are close in value.
#
#           rel_tol
#             maximum difference for being considered "close", relative to the
#             magnitude of the input values
#           abs_tol
#             maximum difference for being considered "close", regardless of the
#             magnitude of the input values
#
#         Return True if a is close in value to b, and False otherwise.
#
#         For the values to be considered close, the difference between them
#         must be smaller than at least one of the tolerances.
#
#         -inf, inf and NaN behave similarly to the IEEE 754 Standard.  That
#         is, NaN is not close to anything, even itself.  inf and -inf are
#         only close to themselves.
#
#     isfinite(x, /)
#         Return True if x is neither an infinity nor a NaN, and False otherwise.
#
#     isinf(x, /)
#         Return True if x is a positive or negative infinity, and False otherwise.
#
#     isnan(x, /)
#         Return True if x is a NaN (not a number), and False otherwise.
#
#     isqrt(n, /)
#         Return the integer part of the square root of the input.
#
#     lcm(*integers)
#         Least Common Multiple.
#
#     ldexp(x, i, /)
#         Return x * (2**i).
#
#         This is essentially the inverse of frexp().
#
#     lgamma(x, /)
#         Natural logarithm of absolute value of Gamma function at x.
#
#     log(...)
#         log(x, [base=math.e])
#         Return the logarithm of x to the given base.
#
#         If the base not specified, returns the natural logarithm (base e) of x.
#
#     log10(x, /)
#         Return the base 10 logarithm of x.
#
#     log1p(x, /)
#         Return the natural logarithm of 1+x (base e).
#
#         The result is computed in a way which is accurate for x near zero.
#
#     log2(x, /)
#         Return the base 2 logarithm of x.
#
#     modf(x, /)
#         Return the fractional and integer parts of x.
#
#         Both results carry the sign of x and are floats.
#
#     nextafter(x, y, /)
#         Return the next floating-point value after x towards y.
#
#     perm(n, k=None, /)
#         Number of ways to choose k items from n items without repetition and with order.
#
#         Evaluates to n! / (n - k)! when k <= n and evaluates
#         to zero when k > n.
#
#         If k is not specified or is None, then k defaults to n
#         and the function returns n!.
#
#         Raises TypeError if either of the arguments are not integers.
#         Raises ValueError if either of the arguments are negative.
#
#     pow(x, y, /)
#         Return x**y (x to the power of y).
#
#     prod(iterable, /, *, start=1)
#         Calculate the product of all the elements in the input iterable.
#
#         The default start value for the product is 1.
#
#         When the iterable is empty, return the start value.  This function is
#         intended specifically for use with numeric values and may reject
#         non-numeric types.
#
#     radians(x, /)
#         Convert angle x from degrees to radians.
#
#     remainder(x, y, /)
#         Difference between x and the closest integer multiple of y.
#
#         Return x - n*y where n*y is the closest integer multiple of y.
#         In the case where x is exactly halfway between two multiples of
#         y, the nearest even value of n is used. The result is always exact.
#
#     sin(x, /)
#         Return the sine of x (measured in radians).
#
#     sinh(x, /)
#         Return the hyperbolic sine of x.
#
#     sqrt(x, /)
#         Return the square root of x.
#
#     tan(x, /)
#         Return the tangent of x (measured in radians).
#
#     tanh(x, /)
#         Return the hyperbolic tangent of x.
#
#     trunc(x, /)
#         Truncates the Real x to the nearest Integral toward 0.
#
#         Uses the __trunc__ magic method.
#
#     ulp(x, /)
#         Return the value of the least significant bit of the float x.
#
# DATA
#     e = 2.718281828459045
#     inf = inf
#     nan = nan
#     pi = 3.141592653589793
#     tau = 6.283185307179586
#
# FILE
#     (built-in)

############################################################

# print(math.factorial(5)) # burada math modülün faktoriyel fonksiyonunu kullandık. modülün içersine yer alan
# # fonksiyonu kullanmak için modüladı.fonksiyonadı şeklinde olmalıdır. burada da olduğu gibi math.factorial gibi.
# # bu örnekte 5 in faktöriyelini hesaplatıp ekrana bastırdık.
# print(math.floor(5.6)) # bu örnekte 5.6 değerini tabana yuvarladık.
# print(math.ceil(5.6)) # bu örnekte 5.6 değerini tavana yuvarladık
#
# # çıktı:
#
# # 120
# # 5
# # 6

###############################################################

# import math as m # burada şunu yaptık: math modülünü import ile programımızın içerisine dahil ettik fakat biz bu math
# # modülünü bundan sonra math ismi ile değilde m ismi ile kullanacağımızı belirttik. aşaşğıdaki örenkeler de math uzun
# # ismini belirtmek yerine m kısa ismi ile kullandık.
#
# print(m.ceil(5.6))
# print(m.floor(5.6))
# print(m.factorial(5))
#
# #çıktı
#
# # 6
# # 5
# # 120

##################################################################

# from math import * # bu yöntem ile math modlü içerisinde ne kadar fonskiyon varsa hepsini programımıza dahil etmek
# # istediğimizi belirtiyoruz. böylelikle budan sonraki yapacağımız işlemlerde math modülü içersinde yer alan
# # fonskiyonları kullanırken bir daha math.fonksiyon adı şeklinde bir yapı yazmamıza gerek kalmıyor. bunun yerine direk
# # fonskiyon adını kullanarak işlem yapabiliyoruz.
#
# print(factorial(5))
# print(ceil(5.6))
# print(floor(5.6))
#
# # çıktı
#
# # 120
# # 6
# # 5

######################################################################

# from math import factorial, floor # burada şunu yaptık: math modülünün bütün fonksiyonları yerine sadece işime yarayan
# # istediğim ksıımlarını almamızı sağladık. bu örenkte olduğu gibi math modlünün sadece facktöriyel
# # ve tavana yuvarlama fonskiyonunu aldık.
#
# print(factorial(5))
# print(floor(5.6))
# print(ceil(5.6)) #  bu fonksiyon math modlü içerisinden alınmadığı için çalışmadı ve hata verdi.
#
# # çıktı:
# # 120
# # 5
# # Traceback (most recent call last):
# #   File "D:\PYTHON\kotlamalar 2\test50.py", line 357, in <module>
# #     print(ceil)
# # NameError: name 'ceil' is not defined

########################################################################

"""

python da
def faktöriyel ():
    kod bloğu
    kod bloğu
    kod bloğu
şeklinde bir fonskiyon tanımladık.

daha sonra da devam eden kod satırlarında ise

from import math * ile math modülünün bütün fonskiyonlarını programa dahil ettik.

faktöriyel (sayı)
şeklinde fonksiyonu çalıştırdığımızda program en son dahil edilen " from import math * " math modünün fonskiyonlarını
kullanarak işlem yapar.

def ile tanımlanan kod bloğu çalışmaz.



"""






















