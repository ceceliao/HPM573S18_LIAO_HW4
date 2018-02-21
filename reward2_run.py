import reward as Cls

pop_size= 1000
n_time_steps=20
coin_prob=0.4

myCohort = Cls.cohort(id=1, pop_size=pop_size, coin_prob=coin_prob)

myCohort.simulate(n_time_steps)


print ('average of these realizations', myCohort.get_reward())
