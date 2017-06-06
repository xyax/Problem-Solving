__author__ = 'xyax'

p= 1,2
print p
x= 0
y= x*(-1)
print y
# print "pto: %d, %d\nv: %d, %d" % (x, y, vx, vy)

"""
            D:
            01>10:
                x=y, y=x*(-1)
            10>0-1:
                x=y, y=x*(-1)
            0-1>-10:
                x=y, y=x*(-1)
            -10>01:
                x=y, y=x*(-1)
            """

"""
             E:
            01>-10:
                x=y*(-1), y=x
            -10>0-1:
                x=y*(-1), y=x
            0-1>10:
                x=y*(-1), y=x
            10>01:
                x=y*(-1), y=x
            """