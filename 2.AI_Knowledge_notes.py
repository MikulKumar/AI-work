'''
knowledge-based agents:
agents that reason by operating on internal representations of knowledge.


*logical reasoning*

terminologies:

sentence: an assertion about the world in a knowledge representation language

propositional logic
    propositional symbols
    P    Q   R 
    each of these symbols represent some fact about the world
    
    to connect these symbols we need connectives

    Logical connectives
    not, and , or , implication , biconditional


    Not:
    
        if P is True then notP is False
        if P is False then notP is True
        the opposite of the sentence 

    And:

        P       Q       PandQ
        false   false   false
        false   true    false
        true    false   false
        true    true    true
    
    Or:
        
        P       Q       PorQ
        false   false   false
        false   true    true
        true    false   true
        true    true    true
    
    implication(->)
        
        if P is true then Q is also true 

        P       Q       P->Q
        false   false   true
        false   true    true 
        true    false   false
        true    true    true

    Biconditional(<->)

        if and only if 

        P       Q       P<->Q
        false   false   true
        false   true    false
        true    false   false
        true    true    true

model:
    assignment of a truth value to every propositional symbol (a "possible world")
    eg:
        P: it is raining
        Q: it is a tuesday

        {P=True,Q=False}
    

    how to represent all of these??

knowledge base(KB):
    a set of sentence known by a knowledge-based agent 

Entailment:
        alpha |= beta
    In every model in which sentence alpha is true sentence beta is also true.
    eg:
        alpha= it is a tuesday in january 
        then 
        beta= it is january
        cause in all worlds where it is a tuesday in january , it is also january
    
Inference:
    the process of deriving new sentences from old ones
    
How do you embedd this into AI


    P: it is a Tuesday 
    Q: it is raining
    R: Harry will go for a run

    KB: (P and notQ) -> R
        if it is a tuesday and it is not raining then Harry will go for a run

        p-True     notQ-True

    Inference: R-True

    Does KB |= alpha ?
    is aplha True?

    Model Checking:
    -To determine if KB |= alpha:
        -Enumerate all possible models
        -If in every model where KB is true , alpha is true, then KB entails alpha.
        -Otherwise, KB does not entail alpha

    
    p: it is a tuesday  Q: it is raining  R: Harry will go for a run
    KB: (P and notQ) -> R       P-True      notQ-True

    Query:  R
      P       Q       R       KB
    false   false   false   false
    false   false   true    false
    false   true    false   false
    false   true    true    false
    true    false   false   false
    true    false   true    true
    true    true    false   false
    true    true    true    false

Knowledge Engineering
    taking a problem and figuring out how to distill it down into knowledge that
    is representable by a computer

prepositional logic deals with the structre and truth values of declarative statements,
while inference rules are the procedures used to derive new statements from existing ones

Inference rules:

    1.Modus ponens
        alpha --> Beta
        if alpha is true then we can tell beta is true too

        eg:
        If it is raining , then Harry is inside 
        we know that "it is raining" is true
        then we know that "Harry is inside" is also true

    2.And Elimination
        aplha or beta is true then
        just alpha is true 
        or likewise
        just beta is true

        eg:
        Harry is friends with Ron and Hermoine
        if is is true then
        Harry is friends with Hermoine 
        is also true

    3.Double Negation Elimination
        not(notAlpha) --> alpha
        two false equals to a true

        eg:
        It is not true that Harry did not pass the test.
        this means that 
        Harry passed the test
    
    4.Implication Elimination
        Alpha --> Beta 
        then 
        notAlpha or Beta 
        Either alpha is not true or beta is true 
        this is a way of transforming if then statements to "or" statements

        eg:
        If it is raining, then Harry is inside
        which would be
        It is not raining or Harry is inside
    
    5.Biconditional Elimination
        Alpha <-->(biconditional) Beta
        then 
        Alpha --> Beta and Beta --> alpha  
        this is a way of transforming Biconditional to smaller symbols

        eg:
        It is raining and if only if Harry is inside 
        then 
        If it is raining, then Harry is inside and if Harry is inside, then it is raining

    6.De Morgan's Law
        not(Alpha and Beta)
        then 
        notAlpha or notBeta
        a way of transforming and's into or's

        eg:
        It is not true that both Harry and Ron passed the test
        then 
        Harry did not pass the test or Ron did not pass the test
    
    7.De Morgan's Law
        not(Aplha or Beta)
        then 
        notAlpha and notBeta

        eg:
        It is not true that Harry or Ron passed the test
        then
        Harry did not pass the test and Ron did not pass the test

    8.Distributive Property
        (Alpha and (Beta or Gamma))
        then 
        (Alpha and Beta) or (Alpha and Gamma)
        ,
        (Alpha or (Beta and Gamma))
        then 
        (Alpha or Beta) and (Alpha or Gamma)

Theorem Proving 
    -initial state: Starting knowledge base 
    -actions: inference rules 
    -transition model: new knowledge base after inference 
    -goal test: ceck statement we're trying to prove
    -path cost function: number of steps in proof

Resolution rule:

    P(True) or Q(True)
       notP(False)
    then 
    Q(True)

    eg:
    (Ron is in the Great Hall) or (Hermione is in the library)
    (Ron is not in the Great Hall)
    then 
    Hermione is in the library



       P or Q 
    notP or R
    then 
       Q or R 

    eg:
    (Ron is in the Great Hall) or (Hermione is in the library)
    (Ron is not in the Great Hall) or (Harry is sleeping)
    then 
    (Hermione is in the library) or (Harry is sleeping)

clause:
    a disjunction of literals
    (disjunction means symbols are connected with "or")
    (literal is a propostional symbol or not of a propositional symbol)
    eg: P or Q or R

Conjuctive normal form:
    logical sentence that is a conjunction of clauses
    (conjunction means the symbols are connected with "and")
    eg: (A or B or C) and (D or notE) and (F or G)

Conversion to CNF(pathway)
    -Elimninate biconditionals
        turn (alpha <--> beta) into (alpha --> Beta) and (Beta --> alpha)
    -Eliminate implications
        turn (alpha --> beta) into notAlpha or Beta
    -Move "not" inwards using De Morgan's Laws 
        eg: turn not(Alpha and Beta) into notAplha or notBeta
    -Use distributive law to destribute "or" wherever possible

    eg:
    (P or Q) --> R 

    not(P or Q) or R                elminate implication

    (notP and notQ) or R            De Morgan's Law 

    (notP or R) and (notQ or R)     Distributive Law
            |
    not it is in Conjunctive normal form 

    but, why even do this ?

    once we have these clauses , these clauses are the inputs 
    for the resolution, inference rule that we saw before 
    If we have 2 clauses and there is something conflicting between them 
    We can resolve them to draw a new conclusion

    this process in called 
    
    Inference by resolution
    (using the resolution rule to draw some sort of inference)

    eg:
    (P --> Q) and P and notQ
    (notP or Q) and P and notQ

    (notP or Q) -> P is False or not
    P -> true 
    then 
    Q -> true 
    P get canceled out
    which means Q is true 

    now we have 
    Q and notQ 
    then  
    nothing or nothing 

    so we get a empty clause 
    the emplty clause represents a contraditction(False). When we derive it, it means:
        The assumptions we started with can't all be true simultaneously
        Since we asumed KB and notQ and found a contradiction 
        This means KB and notQ is unsatisfiable
        Therefore, KB entails Q mus be true.

        In simpler terms, we proved assuming Q is false leads to a contradiction, so Q must be true given our knowledge base.


    Inference by reslotion 
        To deteremine if KB entails Alpha:
            check if (KB entails notAlpha) is a contradtion
                if so, then KB entails Alpha
                Otherwise, no entailment
        
        more concrete example:

        To determine if KB entails Alpha:
            -Convert (KB and notAlpha) to conjuctive Normal Form 
            -Keep checking to see if we can use resolution to produce a new clause
                -If ever we produce the empty clause (equivalent to False), we have a 
                contradiction, and KB entails Alpha.
                -Otherwise, if we can't add new caluses, no entailment.

        Question
        Does (A or B) and (notB and C) and (notC) entails A 

        (A or B) and (notB and C) and (notC) and notA
        4 different clauses 
        (A or B)  (notB or C) (notC) (notA)
          1             2       3       4
        we can resolve clause 2 and 3 

        (A or B) (notA)  (notB)
            1       2       3

        we can resolve clause 1 and 2

        (B) (notB)
          1   2
        
        we can resolve clause 1 and 2 

        ()

        we get a empty clause (contradiction)
        which means KB does not entail notA
        so, KB will entails A  

    
This is called propositional logic 

but we can do better than this 


First-Order Logic 
    there are two types of sybols 
    -Constant Symbol
    eg:
    Minerva, Pomona, Horace, Glideroy, Gryffindor, Hufflepuff, Ravenclaw, Slytherin
    -Predicate Symbol
    eg:
    Person, House, BelongsTo


    Person(Minerva)     Minerva is a person 
    House(Gryffindor)   Gryffindor is a house
    notHouse(Minerva)   Minerva is not a house
    BelongsTo(Minerva, Gryffindor)  Minerva belongs to Gryffindor


    Qunatifiers
        -Universal Quantifiers
            Ax means for all values of x the statement is true.
            Ax.BelongsTo(x,Gryffindor)--> not(BelongsTo(x,Hufflepuff))
        
            in english:
            For all objects x, if x belongs to Gryffindor then x does not belong to Hufflepuff
            or 
            Anyone in Gryffindor is not in Hufflepuff

        -Existential Quantification
            Ex. House(x) and BelongsTo(Minerva,x)
            Ex means there exists a object in x 

            in english:
            There exists an object x such that x is a house and Minerva belongs to x


        Ax.Person(x) --> (Ey.House(y) and BelongsTo(x,y))
        
        for all objects x , if x is a person, then there exsts an object y uch that y is a house and x belongs to y.

all this is to be able to represent logic and be able to reason on that knowledge and draw conclusions and 
        
all of it is just in the same pursuit of the same goal which is representation of knowledge , we want our AI agents to 
be able to know information, to represent that knowledge using prepositional logic , First-Order Logic or some other logic 
and be able to reason on that and draw conclusions make inferences and figure out whether there is some sort of entailment relationship
as by using some inference algorithm like inference by resolution, model checking or any number of these algorithms we can use in order 
to take information that we know and translate it into additional conclusions 

from all this an AI can represent information about what it knows and what it doesnt know


'''
# v = or
'''
question 1
KB: (P → Q) ∧ (¬R → ¬Q) ∧ ¬R
Query: ¬P

(P → Q) ∧ (¬R → ¬Q) ∧ ¬R ∧ P
¬P v Q  ∧  R v ¬Q  ∧ ¬R ∧ P
{} -- empty clause

as we get a empty clause on if it entails P, which means that it is false that KB entails P
it will entail ¬P

question 2
Transform the following statement into Conjunctive Normal Form (CNF):
(P → Q) ∨ (R ∧ ¬S)
(P → Q) v R  ∧  (P → Q) v ¬S
(¬P v Q v R)  ∧  (¬P v Q v ¬S)
correct 

question 3 
Use resolution to determine if the following entailment holds:
KB: (P ∨ Q) ∧ (¬P ∨ R) ∧ (¬Q ∨ ¬R)
Query: P

P ∨ Q ∧ ¬P ∨ R ∧ ¬Q ∨ ¬R ∧ ¬P

P 

KB does entail P 


Question 4
Translate these English sentences into First-Order Logic:
    -All programmers who know Python are employable
    -Some AI researchers don't know Python
    -All employable people earn good salaries
    -Can you prove that some AI researchers don't earn good salaries?

Programmers(x)
AIResearchers(s)
KnowPython(x)
Employable(x)
Goodsalaries(x)

Domain: all people


Ax.programmers(x) and knowPython(x) --> employable(x)
Ex.AIResearchers(x) --> not(KnowPython(x))
Ax.Employable(x) --> Goodsalaries(x)

Ex.AIResearchers(x) and not(Goodsalaries(x))

As AIresearchers are not programmers they do not earn good salaries
