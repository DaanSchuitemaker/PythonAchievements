trees = 333
print("aantal bomen:", trees)
shadedTrees = 333 / 2 / 3
print("aantal bomen in schaduw:", shadedTrees)
sunnyTrees = 333 / 3
print("aantal bomen in zon", sunnyTrees)

shadeOutputModifier  = 0.8

sunnyTreeOutput = 146
print("aantal appels per boom in zon:", sunnyTreeOutput)
shadedTreeOutput = 146 * shadeOutputModifier
print("aantal appels per boom in schaduw:", shadedTreeOutput)

sunnyOutput = sunnyTrees * sunnyTreeOutput
print("totaal aantal appels van bomen in zon:", sunnyOutput)
shadedOutput = shadedTrees * shadedTreeOutput
print("totaal aantal appels van bomen in schaduw:", shadedOutput)
totalOutput = sunnyOutput + shadedOutput
print("totaal aantal appels:", totalOutput)

owners = 4
print("aantal eigenaren:", owners)

myCut = totalOutput / owners
print("aantal appels van mij:", myCut)


