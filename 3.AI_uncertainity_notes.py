'''
Uncertainty
    it refers to the state od limited or incomplete knowledge where it's impossible to 
    precisely determine the truth of statement, predict outcomes
    or describe the exact state of a system.

Probability
    possible worlds(w)-omega
    each of these worlds has a probability to become true 

    P(w) - probability or world

    0 <= p(w) <= 1


Unconditional Probability 
    degree of belief in a proposition
    in te absence of any other evidence 

Conditional probability
    degree of belief in a proposition
    given some evidence that has already been revealed 

    p(a|b) - probability that a is true given the probability that b is already true
    eg:

        p(rain today|rain yesterday) - probability that it rained today given that it rained yesterday 

        p(route change|traffic conditions)
    
        p(disease|test results)


p(a|b) = p(a and b) / p(b) ------- formula

eg:

p(sum 12|sum) --- what is the prob that the second dice rolls to have a sum 12 while one dice is already 6 

p(sum 12|sum) = p(sum12 and 6) / p(6) 

=>              1/36 / 1/6  == 1/6

Random variable
    a variable in probability theory with a domain
    of possible values it can take on.

    eg:
    Roll = {1,2,3,4,5,6},
    Weather = {sun, cloud, rain, wind, snow}
    traffic = {none,light,heavy}

    Flight = {on time, delayed, cancelled}
    probability distribution of the flight variable

    P(Flight = on time) = 0.6
    P(Flight = delayed) = 0.3
    P(Flight = cancelled) = 0.1

    Alternate way to represent this

    capital P means pobability distribution
    P(Flight) = <0.6,0.3,0.1>
                    |
                  vector
    
Independence 
the knowledge that one event occurs does not affect the probability of the other event 
(some event does not increase the chance that some other event might happen)

p(a and b) = p(a).P(b|a) -- dependent 

if a and b were independent then
it would look like
p(a and b) = p(a).P(b) -- independent 

eg:
context: a dice roll

2 dices 
p(6 and a 6) = p(6).p(6)  -- independent 
             = 1/6 x 1/6
             = 1/36

1 dice
p(6 and a 4) =! p(6)p(4)  -- dependent 
there is no way that you can get a 6 and 4 
in the same dice roll
but if we wanted to calculate it 

p(6 and a 4) =! p(6).p(4|6)
             = 1/6 x 0
             = 0 


Bayes' Rule(important rule)

derivation
    p(a and b) = p(b) p(a|b)

    p(a and b) = p(a) p(b|a)

    p(a) p(a|b) = p(b) p(b|a)

    p(b|a) = p(b) . p(a|b) / p(a) -- Bayes' rule


situation:

cloudy in the AM
raining in the PM

given clouds in the morning, 
what's the probability of rain in the afternoon?

info:
    80% of rainy afternoons start with cloudy mornings.
    40% of days have cloudy mornings
    10% of days have rainy afternoons


P(rain|cloud) = P(clouds|rain)xP(rain) / P(clouds)

              = (.8)(.1) / .4
              = 0.2


Knowing:

    P(cloudy morning|rainy afternoon)

we can calculate:

    P(rainy afternoon|cloudy morning)


generally:

    P(visible effect|unknown cause)

we can calculate:

    P(unknown cause|visible effect)


Knowing:

    P(medical test result|disease)

we can calculate:

    P(disease|medical test result)



Joint probability:

    clouds in the morning:
        C = Cloud = 0.4
        C = notCloud = 0.6
    
    raining in the afternoon
        R = Rain = 0.1
        R = notRain = 0.9

    joint probability 

                 R = rain    R = notrain
    C = cloud     0.08          0.32
    C = notcloud  0.02          0.58


P(C|rain) = P(C, rain)  / P(rain)  = alpha.P(C,rain) 
          = alpha.<0.08,0.02> = <0.8,0.2>
            alpha=10

Probability rules

    -Negation:
        P(nota) = 1 - P(a)
    
    -Inclusion-Exclusion
        P(a v b) = P(a) + P(b) - P(a and b)

    -Marginalization
        P(a) = P(a,b) + P(a,notb) # for boolen(True and False)

        P(X = xi) = summation(j,( P( X = xi , Y = yj )) # more practical

    Eg:
                     R = rain    R = notrain
        C = cloud     0.08          0.32
        C = notcloud  0.02          0.58

        P(C=cloud) = P(C=cloud,r=rain) + P(C=cloud,R=notrain)
                   = 0.08 + 0.32
                   = 0.40
        joint probability to single probability 

    -Conditioning
        P(a) = P(a|b).P(b) + P(a|notb).P(notb)

        P(X - xi) = Summation(j,( P( X = xi| Y = yj ).P(Y=yj)))

    


Bayesian network:
    data structure that represents the 
    dependencies among random variables 

Bayesian network
    -directed graph
    -each nodes represnt a random variable
    -arrow from X to Y means X is a parent of Y
    -each node X has probability distribution
     P(X| Parents(X))
    


            Rain
     {none, light, heavy}
        |           |
        v           |
    Maintenance     |
    {yes,no}        |
        |           |
        v           v
            train
        {on time, delayed}
            |
            |
            v
        Appointment
        {attend,miss}



there is dependencies 
me being on time for the appointment is dependent
upon train reaching on time or being delayed
and that is dependent upon 2 things 
maintenance and rain.


lets begin with the first node

           Rain
     {none, light, heavy}

none = 0.7
light = 0.2
heavy = 0.1

now , the second node
    Maintenance     
     {yes,no}

        yes     no 
none    0.4     0.6
light   0.2     0.8
heavy   0.1     0.9

this now becomes a conditional probability


now, the third node

    you get it probably 
    another table , that i dont want to type

now, the last one

      T      attend      miss
    on time   0.9        0.1
    delayed   0.6        0.4

