B = 10.0/(40*8*24)
j = 3.0/(15*24)

t0 = 0.0

dt = 8

D = 30 # Simulate for D days

tN = int(D*24) # Corresponding no of hours

R = int(round((tN - t0)/dt))

t = linspace(t0, tN, R+1)

#Defining empty arrays
S_H = zeros(R+1)
I_H = zeros(R+1)
R_H = zeros(R+1)

S_E = zeros(R+1)
I_E = zeros(R+1)
R_E = zeros(R+1)

#Initial values
S_H[0] = 50
I_H[0] = 1
R_H[0] = 0

S_E[0] = 50
I_E[0] = 1
R_E[0] = 0

# Solving the equations with Heun's method
for n in range(R):
    #Preliminary values to be used to calculate real value
    S_prelim = S_H[n] - B*dt*S_H[n]*I_H[n]
    I_prelim = I_H[n] + B*dt*S_H[n]*I_H[n] - j*dt*I_H[n]
    R_prelim = R_H[n] + j*dt*I_H[n]

    #Calculating real next value
    S_H[n+1] = S_H[n] - B*dt*((S_prelim*I_prelim) + (S_H[n]*I_H[n]))/2.0
    I_H[n+1] = I_H[n] + B*dt*((S_prelim*I_prelim) + (S_H[n]*I_H[n]))/2.0 - j*dt*(I_prelim + I_H[n])/2.0
    R_H[n+1] = R_H[n] + j*dt*(I_prelim + I_H[n])/2.0

    # Solving with Eulers forward  
for n in range(R):
    S_E[n+1] = S_E[n] - B*dt*S_E[n]*I_E[n]
    I_E[n+1] = I_E[n] + B*dt*S_E[n]*I_E[n] - j*dt*I_E[n]
    R_E[n+1] = R_E[n] + j*dt*I_E[n]

plt.subplot(212)
plt.ylabel('People')
plt.xlabel('Time [hours]')
plt.plot(t, S_H, label = 'Heun_suseptible') 
plt.plot(t, I_H, label = 'Heun_infected')
plt.plot(t, R_H, label = 'Heun_resitants')

plt.plot(t, S_E, label = 'FE_suseptible') 
plt.plot(t, I_E, label = 'FE_infected')
plt.plot(t, R_E, label = 'FE_resitants')
plt.legend()