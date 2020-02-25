# from flask import Flask,request,jsonify
# from flask_cors import CORS
#
# from bert import QA
#
# app = Flask(__name__)
# CORS(app)
#
# model = QA("model")
#
# @app.route("/predict",methods=['POST'])
# def predict():
#     doc = request.json["document"]
#     q = request.json["question"]
#     try:
#         out = model.predict(doc,q)
#         return jsonify({"result":out})
#     except Exception as e:
#         print(e)
#         return jsonify({"result":"Model Failed"})
#
# if __name__ == "__main__":
#     app.run('0.0.0.0',port=8000)


from bert import QA

model = QA('model')

doc = "Organizations of different sizes, operating in myriad industries and geographies, do not consistently use the terms “sourcing,” “procurement” and “vendor (or supplier) management.” This often leads to miscommunication when the organization interacts with partners, suppliers, customers or other third parties. There is not one common or universally accepted use of terminology or organizational structure. Therefore, the focus should be on building the right muscles in the key disciplines and ensuring the various teams are working together synergistically to optimize value of indirect technology spend. \
This can be achieved only when the disciplines of sourcing, procurement and vendor management have clearly delineated authority, have documented roles and responsibilities, and work together to plan and execute these objectives. Gartner views each discipline as having a unique and important contribution to an organization’s ability to strategize, engage and optimize vendor offerings, solutions and performance. When these disciplines operate in separate, siloed divisions, or are missing entirely, tensions and capability gaps can develop, undermining the effectiveness of these functions. This, in turn, can lead to either the bypassing of SPVM due to perceived irrelevance or vendors using “divide and conquer” tactics. \
The first imperative regarding the three disciplines is that they are like cogs in a machine, working together and relying on each other to create value. \
SPVM leaders must ensure a comprehensive, collaborative approach in order to realize efficiency, efficacy and agility that consistently deliver on strategic business outcomes.The Key Disciplines for the Procurement Function are Strategize, Purchase and Manage. \
Sourcing strategies focus on designing the blueprint for architecting the procurement deals, organizational competencies/changes, governance, risk and synergistic approaches to optimally balance cross-category elements of the business and IT solutions that will come together to enable results. The actual deliverable is often not a single document or slide deck. Hence, our definition above describes a set of scenarios, directives, business cases and decisions that are dynamic. We say “define and refine” to emphasize the iterative approach that is needed to stay abreast of market disruption, vendor activity and dynamic needs of the business. The most important element of these iterations is to focus on stakeholder satisfaction, measurement, risk and governance that will generate and sustain the most business value. \
The critical work in the market intelligence area includes identifying high-level products, solutions and service options in order to analyze the these variables i.e. Market maturity,Volatility,Risk elements,Price elasticity,Availability by geographic region,Potential industry-specific or regulatory issues. \
The Strategize Discipline must align to the business and IT goals for enabling the processes and functional areas of the organization. The strategies cannot be static, but rather, they must be continually evaluated, revised and measured against changing business priorities, market disruptions and new opportunities. They then must be endorsed by stakeholders across the organization. \
In Gartner’s key disciplines for the procurement function, the Strategize Discipline focuses primarily on sourcing strategies for business and IT solutions. Additionally, those organizations that also use category planning should map their spending back to the overall budgeting process. A large majority of Gartner client inquiries are focused on practical planning and operationalizing of the strategy. \
The Key Activities of Strategize Discipline includes Analyze Demand, Analyze Financials, Market Intelligence and Sourcing Options, Define and Refine Sourcing Strategy, Operationalize Strategy. \
The Purchase Discipline should be a structured and standardized set of activities designed for processing a large volume of transactions at a speed that enables business and IT teams to deliver  results. Therefore, purchasing must be repeatable and clearly understood by the teams executing the transactions, as well as transparent to the stakeholders who receive the results."

q = 'What is the work of market intelligence??'

answer = model.predict(doc,q)

print(answer['answer'])
# 1975
# print(answer.keys())
# dict_keys(['answer', 'start', 'end', 'confidence', 'document']))