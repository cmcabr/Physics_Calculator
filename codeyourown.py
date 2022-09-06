"""
Automation
Student Project
Project Title: Physics Equation Calculator
Craig Cabrera
"""

# These are a few values which I have used for testing, which have worked for the below situations:
# xi = 5
# xf = 257
# vi = 12
# vf = 72
# a = 10
# t = 6
# m = 8
# p = 576
# mu = 0.6
# F = 80 * 0.6 = 48
# const = 48/5 = 9.6

# Libraries
import math

# Defining global variables for later use.
# Values are for math, checks are for what we are solving for.
xf = 0
xf_check = False
xi = 0
xi_check = False
vf = 0
vf_check = False
vi = 0
vi_check = False
a = 0
a_check = False
t = 0
t_check = False
p = 0
p_check = False
m = 0
m_check = False
const = 0
const_check = False
mu = 0
mu_check = False
F = 0
F_check = False
K = 0
K_check =  False
U = 0
U_check = False
g = 9.81

# Introduction Menu
print("Welcome to the Physics Equation Calculator.")
print()
print("What do you want to solve for?")
print("  a) Velocity-Time Formula")
print("  b) Position-Time Formula")
print("  c) Velocity-Position Formula")
print("  d) Momentum")
print("  e) Force")
print()
formula = input("Your Input: ")
print()

# Velocity-Time Formula
if formula == "a":
    # Introduction on how the formula is found.
    print("--------------------------------------------------------------------------------------------------------------------------------------------")
    print("The velocity-time formula is used to show the relation between velocity, acceleration, and time. It is expressed through the formula")
    print()
    print("vf = v₀ + at, t ≥ 0")
    print()
    print("where vf is final velocity, v₀ is initial velocity, a is acceleration, and t is time. Remember that velocity is change in position ")
    print("with respect to time, and acceleration is change in velocity with respect to time.")
    print()
    print("This formula comes from the definition of acceleration in physics. The derivation for the formula is shown below, where d represents change:")
    print()
    print("a = dv/dt")
    print("  = (vf - vi) / dt")
    print("at = vf - vi")
    print("at + vi = vf")
    print()
    print("While this equation does show dt, change in time, rather than total time, it is important to note that vi, initial velocity, is instead ")
    print("simplified to v₀, or velocity when t = 0. This then means that dt = t - t₀, or change in time from t = 0 to final time.")
    print()
    print("It is also important to note that this formula is usually used for vertical velocity, or movement from left to right, since there is no ")
    print("horizontal acceleration in most projectile motion questions.")
    print()
    print("--------------------------------------------------------------------------------------------------------------------------------------------")
    # Calculator
    continuation = input("Below is your calculator, if you would like. Press enter for the value you are solving for. Press enter to continue.") == ""
    print()
    if continuation:
        print("First, let us check what values you have. Remember SI Units. ")
        print()
        vf = input("What is the final velocity? If you instead have a change in velocity value, write it here. ")
        print()
        vi = input("What is the initial velocity? If you instead have a change in velocity value, enter it as zero. ")
        print()
        t = input("What is the time change?  ")
        print()
        a = input("What is the acceleration? ")
        print()
        # Checking for valid answers.
        if vf != "":
            vf_check = True
        if vi != "":
            vi_check = True
        if t != "":
            t_check = True
        if a != "":
            a_check = True
        if vf_check and vi_check and a_check and t_check:
            print("Let's check your work.\n")
            vf_calc = float(vi) + float(a)*float(t)
            print("Your calculated final velocity: " + str(float(vi) + float(a)*float(t)))
            print("Your given final velocity: " + vf)
            print(str(vf_calc) + " = " + vf + "\n")
            if math.floor(float(vf_calc)) == math.floor(float(vf)):
                print("That's right!")
            else:
                print("Something's not right. Try again next time.")
        elif vi_check and t_check and a_check:
            print("Let's solve for final velocity.\n")
            print("vf = " + vi + " + " + a + "*" + t + "\n")
            print("Your value for final velocity is: " + str(float(vi) + float(a)*float(t)))
        elif vf_check and t_check and a_check:
            print("Let's solve for initial velocity.\n")
            print("vi = " + vf + " - " + a + "*" + t + "\n")
            print("Your value for initial velocity is: " + str(float(vf) - (float(a)*float(t))) + "\n")
        elif vf_check and vi_check and t_check:
            print("Let's solve for acceleration.\n")
            print("a = " + "(" + vf + " - " + vi + ") / " + t + "\n")
            print("Your value for acceleration is: " + str((float(vf) - float(vi))/float(t)) + "\n")
        elif vf_check and vi_check and a_check:
            print("Let's solve for time.\n")
            print("t = " + "(" + vf + " - " + vi + ") / " + a + "\n")
            print("Your value for time is: " + str((float(vf) - float(vi))/float(a)) + "\n")
        else:
            print("Either you did not put enough values in or entered a phrase instead. Better luck next time.")

# Position-Time Formula
elif formula == "b":
    # Introduction on how the formula is found.
    print("--------------------------------------------------------------------------------------------------------------------------------------------")
    print("The formula is used to show the relation between velocity, acceleration, and time. It is expressed through the formula:")
    print()
    print("xf = x₀ + v₀t + 0.5at², t ≥ 0")
    print()
    print("where xf is final position, x₀ is initial position, v₀ is initial velocity, a is acceleration, and t is time. ")
    print("This formula comes from the definitions of acceleration of velocity and acceleration in physics, along with the velocity-time formula.")
    print("The derivation of the formula is shown below, where d represents change:")
    print()
    print("a = dv/dt")
    print("  = (vf - vi) / dt")
    print("at = vf - vi")
    print("at + vi = vf")
    print()
    print("v = dx/dt")
    print("(v)dt  = dx")
    print("∫(at + vi)dt = ∫(dx/dt)dt")
    print("0.5at² + (vi)t = dx = xf - x₀")
    print("0.5at² + (vi)t + xi = xf")
    print()
    print("Once again notice that vi and xi are v₀ and x₀, simplifying initial velocity and initial position to the position and velocity at t = 0. One ")
    print("helpful hint on such an equation: in most projectile motion questions, x₀ = 0, and a = 0 when solving for the x-direction and a = 9.8 when ")
    print("solving for the y-direction.")
    print()
    print("--------------------------------------------------------------------------------------------------------------------------------------------")
    print()
    # Calculator
    continuation = input("Below is your calculator, if you would like. Press enter for the value you are solving for. Press enter to continue.\n") == ""
    if continuation:
        print("First, let us check what values you have. Remember SI Units.")
        print()
        xf = input("What is the final position? If you instead have a change in position value, write it here. ")
        print()
        xi = input("What is the initial position? If you instead have a change in position value, enter it as zero. ")
        print()
        vi = input("What is the initial velocity? ")
        print()
        t = input("What is the time change? ")
        print()
        a = input("What is the acceleration? ")
        print()
        # Checking for valid answers.
        if xf != "":
            xf_check = True
        if xi != "":
            xi_check = True
        if vi != "":
            vi_check = True
        if t != "":
            t_check = True
        if a != "":
            a_check = True
        if xi_check and xf_check and vi_check and t_check and a_check:
            print("Let's check your work.\n")
            xf_calc = float(xi) + float(vi)*float(t) + float(a)*float(t)*float(t)*0.5
            print("Your calculated final position: " + str(xf_calc))
            print("Your given final position: " + xf + "\n")
            print(str(xf_calc) + " = " + str(xf) + "\n")
            if math.floor(xf_calc) == math.floor(float(xf)):
                print("That's right!")
            else:
                print("Something's not right. Try again next time.")
        elif xi_check and vi_check and t_check and a_check:
            print("Let's solve for final position.\n")
            print("xf = " + xi + " + " + vi + "*" + t + " + " + str(0.5*float(a)) + "*" + str(float(t)**2) + "\n")
            print("Your value for final position is: " + str(float(xi) + float(vi)*float(t) + 0.5*float(a)*float(t)*float(t)))
        elif xf_check and vi_check and t_check and a_check:
            print("Let's solve for initial position.\n")
            print("xi = " + xf + " - " + vi + "*" + t + " - 0.5*" + a + "*" + t + "*" + t + "\n")
            print("Your value for initial position is: " + str(float(xf) - float(vi)*float(t) - 0.5*float(a)*float(t)*float(t)))
        elif xf_check and xi_check and t_check and a_check:
            print("Let's solve for initial velocity.\n")
            print("vi = (2*" + xf + " - 2*" + xi + " - " + a + "*" + t + "*" + t + ") / 2*" + t + "\n")
            print("Your value for initial velocity is: " + str(((2*float(xf)) - (2*float(xi)) - (float(a)*float(t)*float(t))) / (2*float(t))))
        elif xf_check and xi_check and vi_check and a_check:
            print("Let's solve for time.\n")
            print("t = (±" + vi + " + √((" + vi + "*" + vi + ") - 2*" + a + "*(" + xi + " - " + xf + "))) / (" + a + ")\n")
            print("HINT: If this formula looks similar, it is using the quadratic formula, with a = a, b = 2v, and c = (2xi - 2xf)")
            print("Your values for time are: " + str(-1*(((float(vi)) + math.sqrt((float(vi) ** 2) - (2*float(a)*(float(xi)-float(xf))))) / (float(a)))) + " and " + str(((float(vi)*-1) + math.sqrt((float(vi) ** 2) - (2*float(a)*(float(xi)-float(xf))))) / (float(a))) + "\n")
        elif xf_check and xi_check and vi_check and t_check:
            print("Let's solve for acceleration.\n")
            print("a = (2*" + xf + " - 2*" + xi + " - 2*" + vi + "*t) / (" + t + "*" + t + ")\n")
            print("Your value for acceleration is: " + str((2*float(xf) - 2*float(xi) - 2*float(vi)*float(t))/(float(t)**2)))
        else:
            print("Either you did not put enough values in or entered a phrase instead. Better luck next time.")

# Velocity-Position Formula
elif formula == "c":
    # Introduction on how the formula is found.
    print("--------------------------------------------------------------------------------------------------------------------------------------------")
    print("The formula is used to show the relation between velocity, acceleration, and change in position. It is expressed through the formula:")
    print()
    print("vf² = vi² + 2adx")
    print()
    print("where vf is final velocity, vi is initial velocity, a is acceleration, and dx is change in position. This formula comes from the ")
    print("definitions of velocity and acceleration, the position-time formula, and the velocity-time formula. The derivation of the formula")
    print("is shown below, where d represents change:")
    print()
    print("vf = vi + at ∴ t = (vf - vi)/a")
    print("xf = (vi)t + 0.5at²")
    print("   = (vi)((vf - vi)/a) + 0.5(a)((vf - vi)/a)²")
    print("   = ((vi)(vf) - vi²)/a + 0.5(vf - vi)((vf - vi)/a)")
    print("2axf = 2((vi)(vf) - vi²) + (vf - vi)²")
    print("     = 2(vi)(vf) - 2vi² + vf² - 2(vi)(vf) + vi²")
    print("     = -vi² + vf²")
    print("2axf + vi² = vf²")
    print()
    print("Notice how in this equation, xf is used as dx since x₀ denotes position of 0, meaning xf = dx.")
    print()
    print("--------------------------------------------------------------------------------------------------------------------------------------------")
    # Calculator
    continuation = input("Below is your calculator, if you would like. Press enter for the value you are solving for. Press enter to continue.\n") == ""
    if continuation:
        print("First, let us check what values you have. Remember SI Units.")
        print()
        vf = input("What is the final velocity? If you instead have a change in velocity value, write it here. ")
        print()
        vi = input("What is the initial velocity? If you instead have a change in velocity value, enter it as zero. ")
        print()
        a = input("What is the acceleration? ")
        print()
        xf = input("What is the change in position? ")
        print()
        if vf != "":
            vf_check = True
        if vi != "":
            vi_check = True
        if xf != "":
            xf_check = True
        if a != "":
            a_check = True

        if vf_check and vi_check and xf_check and a_check:
            print("Let's check your work. \n")
            vf_calc = math.sqrt((float(vi)**2) + 2*float(a)*float(xf))
            print("Your calculated final velocity: " + str(vf_calc))
            print("Your given final velocity: " + vf + "\n")
            print(str(vf_calc) + " = " + str(vf) + "\n")
            if math.floor(vf_calc) == math.floor(float(vf)):
                print("That's right!\n")
            else:
                print("Something's not right. Try again next time.\n")
        elif vi_check and xf_check and a_check:
            print("Let's solve for final velocity.\n")
            print("vf = " + "√(" + vi + "² + 2*" + a + "*" + xf + ")\n")
            print("Your value for final velocity is: " + str(math.sqrt((float(vi)**2) + 2*float(a)*float(xf))) + "\n")
        elif vf_check and xf_check and a_check:
            print("Let's solve for initial velocity.\n")
            print("vi = √(" + vf + "² - 2*" + a + "*" + xf + ")\n")
            print("Your value for initial velocity is: " + str(math.sqrt((float(vf)*float(vf)) - 2*float(a)*float(xf))))
        elif vf_check and vi_check and xf_check:
            print("Let's solve for acceleration.\n")
            print("a = ±√(" + vi + "² + 2*" + a + "*" + d + ")\n")
            print("Your values for acceleration are: " + str(math.sqrt((float(vi**2) + 2*float(a)*float(xf)))) + " and " + str(-1*(math.sqrt((float(vi**2) + 2*float(a)*float(xf)))) + "\n"))
        elif vf_check and vi_check and a_check:
            print("Let's solve for the change in distance.\n")
            print("dx = (" + vf + "² - " + vi + "²) / (2" + a + ")")
            print("Your value for change in distance are: " + str(((float(vf)**2) + (float(vi)**2)) / (float(a)*2)) + "\n")
        else:
            print("Either you did not put enough values in or entered a phrase instead. Better luck next time.")

# Momentum Formula
elif formula == "d":
    # Introduction on how the formula is found.
    print("--------------------------------------------------------------------------------------------------------------------------------------------")
    print("The momentum formula is used to show the relation between mass and velocity. It")
    print("is expressed through the formula:")
    print()
    print("p = mv,")
    print()
    print("where p is momentum, m is mass, and v is the current velocity at the given time.")
    print("This formula comes from the definition of velocity and the definition of force. The")
    print("derivation of the formula is shown below, where d represents change:")
    print()
    print("F = ma")
    print("dp/dt  = m(dv/dt)")
    print("dp*dt/dt = m*dv")
    print("dp = m*dv")
    print()
    print("While not the main focus of this question, it is important to note that impulse, J, ")
    print("is equal to dp, the change in momentum.")
    print()
    print("--------------------------------------------------------------------------------------------------------------------------------------------")

    # Calculator
    continuation = input("Below is your calculator, if you would like. Press enter for the value you are solving for. Press enter to continue.\n") == ""
    if continuation:
        print("First, let us check what values you have. Remember SI Units.\n ")
        p = input("What is the momentum? ")
        print()
        m = input("What is the total mass of the object or system which velocity affects? ")
        print()
        vf = input("What is the velocity of the object or system? ")
        print()
        if p != "":
            p_check = True
        if m != "":
            m_check = True
        if vf != "":
            vf_check = True
        if m_check and vf_check and p_check:
            print("Let's check your work. \n")
            p_calc = float(m)*float(vf)
            print("Your calculated momentum: " + str(p_calc))
            print("Your given momentum: " + p)
            print(str(p_calc) + " = " + p + "\n")
            if math.floor(p_calc) == math.floor(float(p)):
                print("That's right!")
            else:
                print("Something's not right. Try again next time.\n")
        elif m_check and vf_check:
            print("Let's solve for momentum.\n")
            print("p = " + m + "*" + vf + "\n")
            print("Your value for momentum is: " + str(float(m)*float(vf)) + "\n")
            print()
        elif p_check and m_check:
            print("Let's solve for velocity.\n")
            print("v = " + p + "/" + m + "\n")
            print("Your value for velocity is: " + str(float(p)/float(m)) + "\n")
            print()
        elif p_check and vf_check:
            print("Let's solve for mass.\n")
            print("m = " + p + "/" + vf + "\n")
            print("Your value for mass is: " + str(float(p)/float(vf)) + "\n")

# Force
elif formula == "e":
    # Introduction on how the formula is found.
    print("--------------------------------------------------------------------------------------------------------------------------------------------")
    print("The formula is used to show the relation between force, mass, and acceleration. This formula also shows Hooke's Law, a relation between ")
    print("force, and spring compression. It is expressed through the formula:")
    print()
    print("F = μma = -kx")
    print()
    print("where F is force, μ is the frictional coefficient, m is mass, a is acceleration, k is some constant, and x is change in distance (in this ")
    print("case, compression of the spring.) The first formula comes from the definitions of momentum and acceleration in physics. The derivation of ")
    print("the formula is shown below, where d represents change:")
    print()
    print("p = mv")
    print("dp/dt = dmv/dt")
    print("      = ma")
    print("      = F")
    print()
    print("This then can mean that force is the rate of change of momentum.")
    print()
    print("The second formula is known as Hooke's Law, which comes from the Work-Energy Theorem. The derivation of the formula is shown below, where d ")
    print("represents change, PE represents potential energy, KE represents kinetic energy, and r represents spring length (i.e. r = x):")
    print()
    print("Let us define ri = r and rf = r + dr. Then,")
    print("dPE = 0.5k(rf - ri)²")
    print("dPE = 0.5kdr² ")
    print("   = 0.5k(r + dr)² - 0.5k(r)²")
    print("   = krdr + 0.5kdr²")
    print("Now, let us also define dr << 1 ∴ dPE = krdr")
    print("dE = dKE + dPE = 0")
    print("dKE + krdr = 0")
    print("dK = -krdr")
    print("The Work-Energy Theorem states that W = KE = Fdr. Therefore, ")
    print("Fdr = dKE = -krdr")
    print("F = -kr")
    print()
    print("--------------------------------------------------------------------------------------------------------------------------------------------")
    # Calculator
    continuation = input("Below is your calculator, if you would like. Press enter for the value you are solving for. Press enter to continue.\n") == ""
    if continuation:
        print("First, let us check what values you have. Remember SI Units.\n ")
        F = input("What is the force? ")
        print()
        mu = input("What is the frictional coefficient? If there is none, leave this blank. ")
        print()
        m = input("What is the total mass of the object or system which velocity affects? ")
        print()
        a = input("What is the acceleration? ")
        print()
        const = input("What is the spring constant (k)? ")
        print()
        xf = input("What is the compression of the spring? ")
        print()
        if F != "":
            F_check = True
        if mu != "":
            mu_check = True
        if mu == "":
            mu_check = True
            mu = 1
        if m != "":
            m_check = True
        if a != "":
            a_check = True
        if const != "":
            const_check = True
        if xf != "":
            xf_check = True
        if m_check and a_check and mu_check and F_check:
            print("Let's check your work.\n")
            F_calc = float(mu)*float(m)*float(a)
            print("Your calculated force: " + str(F_calc))
            print("Your given force: " + F + "\n")
            print(str(F_calc) + " = " + str(F) + "\n")
            if math.floor(F_calc) == math.floor(float(F)):
                print("That's right!")
            else:
                print("Something's not right. Try again next time.\n")
        elif F_check and const_check and xf_check:
            print("Let's check your work.\n")
            F_calc = float(const)*float(xf)
            print("Your calculated force: " + str(F_calc))
            print("Your given force: " + F + "\n")
            print(str(F_calc) + " = " + str(abs(float(F))) + "\n")
            if math.floor(F_calc) == math.floor(abs(float(F))):
                print("That's right!")
            else:
                print("Something's not right. Try again next time.\n")
        elif m_check and a_check and mu_check and const_check and xf_check:
            print("Let's check your work.\n")
            F_calc = float(mu)*float(m)*float(a)
            Hooke_calc = float(const)*float(xf)
            print("Your normal force: " + str(F_calc))
            print("Your Hookean force: " + str(Hooke_calc) + "\n")
            print(str(F_calc) + " == " + str(Hooke_calc) + "\n")
            if math.floor(F_calc) == math.floor(Hooke_calc):
                print("That's right!")
            else:
                print("Something's not right. Try again next time.\n")
        elif m_check and a_check and mu_check and const_check and xf_check and F_check:
            print("Let's check your work.\n")
            F_calc = float(mu)*float(m)*float(a)
            Hooke_calc = float(const)*float(xf)
            print("Your given force: ")
            print("Your normal force: " + str(F_calc))
            print("Your Hookean force: " + str(Hooke_calc) + "\n")
            print(str(F_calc) + " == " + str(Hooke_calc) + " = " + str(F) + "\n")
            if math.floor(F_calc) == math.floor(Hooke_calc):
                print("Calculated variables check out...")
                if math.floor(F_calc) == math.floor(F):
                    print("That's right!")
            else:
                print("Something's not right. Try again next time.\n")
        elif m_check and const_check and xf_check:
            print("Let's solve for acceleration.\n")
            print("a = (" + const + "*" + x + ") / " + m)
            print("Your value for acceleration is: " + str((float(const)*float(xf)) / float(m)) + "\n")
        elif a_check and const_check and xf_check:
            print("Let's solve for mass. \n")
            print("m = (" + const + "*" + x + ") / " + a)
            print("Your value for mass is: " + str((float(const)*float(xf)) / float(a)) + "\n")
        elif m_check and a_check and const_check:
            print("Let's solve for the spring constant. \n")
            print("k = (" + m + "*" + a + ") / " + x + "\n")
            print("Your value for the spring constant is: " + str((float(m)*float(a)) / float(xf)) + "\n")
        elif m_check and a_check and const_check:
            print("Let's solve for spring compression. \n")
            print("x = (" + m + "*" + a + ") / " + const + "\n")
            print("Your value for spring compression is: " + str((float(m)*float(a)) / float(k)) + "\n")
        elif F_check and m_check and a_check:
            print("Let's solve for the frictional coefficient. \n")
            print("μ = " + F + " / (" + m + "*" + a + ")")
            print("Your value of the frictional coefficient is: " + str(float(F) / (float(m)*float(a))))
        elif m_check and a_check:
            print("Let's solve for force. \n")
            print("F = " + m + "*" + a)
            print("Your value for force is: " + str(float(m)*float(a)))
        elif F_check and a_check:
            print("Let's solve for mass. \n")
            print("m = " + F + " / " + a)
            print("Your value for mass is: " + str(float(F)/float(a)))
        elif F_check and m_check:
            print("Let's solve for acceleration. \n")
            print("a = " + F + " / " + m)
            print("Your value for acceleration is: " + str(float(F)/float(m)))
        elif const_check and xf_check:
            print("Let's solve for force. \n")
            print("F = " + const + "*" + xf)
            print("Your value for force is: " + str(float(k)*float(xf)))
        elif F_check and a_check:
            print("Let's solve for the spring constant. \n")
            print("k = " + F + " / " + xf)
            print("Your value for mass is: " + str(float(F)/float(xf)))
        elif F_check and m_check:
            print("Let's solve for spring compression. \n")
            print("x = " + F + " / " + const)
            print("Your value for spring compression is: " + str(float(F)/float(const)))

else:
    print("Maybe this isn't the right app for you...")

print()
print("--------------------------------------------------------------------------------------------------------------------------------------------")
print()
print("Thank you for using our guide on this formula. We hope this helps you in your studies for physics.")
