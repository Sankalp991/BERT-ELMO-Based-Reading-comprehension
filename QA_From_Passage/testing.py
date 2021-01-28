from bert import QA

model = QA('model')

doc = "Come And See This Beautiful And Well Kept Backsplit With Fully Fenced Yard In This High Demand North York Family-Friendly Neighbourhood. Featuring Upgrades And Updates Galore. This Well Laid Out Home Shows Real Pride Of Ownership. Steps To Schools, Mall, Public Transit, Banks, Ttc And More. The Basement Features An In-Law Suite With Separate Entrance, Bathroom And Kitchen. Kitchen renovated in 2018, Main Bathroom in 2017 And Powder Room in 2018. Parking type is attached garage with 3 parking spaces. Unit has total 3 bathrooms, 4 bedrooms above grade and 1 bedroom below grade. Unit type is semi-detached with backsplit."

# doc = "Victoria has a written constitution enacted in 1975, but based on the 1855 colonial constitution, passed by the United Kingdom Parliament as the Victoria Constitution Act 1855, which establishes the Parliament as the state's law-making body for matters coming under state responsibility. The Victorian Constitution can be amended by the Parliament of Victoria, except for certain 'entrenched' provisions that require either an absolute majority in both houses, a three-fifths majority in both houses, or the approval of the Victorian people in a referendum, depending on the provision."
q = 'What does the basement have?'

answer = model.predict_answer(doc,q)

print(answer['answer'])