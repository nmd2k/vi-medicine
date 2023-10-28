DEFAULT_PROMPT = "You are helpfull AI assistance. User question: {query}"

DIAGNOSE_PROMPT = """The doctor will provide some information about related diseases and a patient's symptoms. 
Your task is to provide a diagnosis with the highest probability based on the provided disease information and the patient's symptoms. 
Explain the diagnosis and make a note of the reference information source.
The conclusion must adhere to the JSON format below:

{"diagnosis": "string", "explain": "string", "source": ["string"]}}

For example:
### Disease's information
Disease A: Information about the disease A
Disease B: Information about the disease B
### Patient's symptom: The patient appear symptom C
### Diagnosis:
{"diagnosis": "Disease A", "explain": "Based on the patient's symptoms and the provided information, the most likely diagnosis is Disease A.", "references": ["Medical Journal X, Page 123", "Medical Journal Y, Page 456"]}
"""

DIAGNOSE_TEMPLATE = """
### Disease's information
{disease_info}
### Patient's symptom: {symptom}
### Diagnosis:
"""

CHECK_MEDICINE_PROMPT = """The doctor will provide the name of a medication, some information about the disease that needs treatment, and documents related to some types of medications.
Your task is to conclude whether that medication is suitable for treating the mentioned disease based on the provided information about the disease and medications.

The conclusion can be one of the following three forms:
- "RELEVANT": if the medication is suitable for treating the disease.
- "IRRELEVANT": if the medication is not suitable for treating the disease.
- "UNDEFINED": if there is not enough information to make a conclusion, and further evaluation by a doctor is needed.

The conclusion must adhere to the JSON format below:
{"review": "string", "explain": "string"}

For example:
### Disease Information
Disease A: Requires treatment with Medication B
### Medication Information:
Medication B can be used to treat Disease A
Medication C cannot be used to treat Disease A
### Target disease: Disease A
### Target medication: Medication C
### Conclusion:
{"review": "IRRELEVANT", "explain": "Medication C is not suitable for treating Disease A"}
"""

CHECK_MEDICINE_TEMPLATE = """
### Disease Information
{disease_doc}
### Medication Information:
{drug_doc}
### Target disease: {disease}
### Target medication: {drug}
### Conclusion:
"""

SUGGEST_MEDICINE_PROMPT = """The doctor will provide the name of a disease that requires treatment and related documents about the disease.
Your task is to provide a conclusion about one medication suitable for treating the mentioned disease, based on the information provided about the disease and medications. 
If there was no specific medication mentioned, conclude "No specific suggestion" and your explanation. 
Additionally, you need to explain the reason for your conclusion. 

The return output must follow to the JSON format below:
{"suggestion": "string", "explain": "string"}

For example:
### Disease Information
Disease A: Requires treatment with Medication B
### Target disease: Disease A
### Suggestion:
{"suggestion": "Medication B", "explain": "Medication B is suitable for treating Disease A because..."}
of
"""

SUGGEST_MEDICINE_TEMPLATE = """
### Disease Information
{disease_info}
### Target disease: {disease}
### Suggestion:
"""

COMPATIBLE_PROMPT = """
The doctor will provide the names of two medications and related medication documents.
Your task is to conclude whether these two medications are suitable for use together based on the provided information about the medications and their relation to the disease.

The conclusion can be one of the following three forms:
"RELEVANT": if the medications are compatible for treating the disease.
"IRRELEVANT": if the medications are not compatible for treating the disease.
"UNDEFINED": if there is not enough information to make a conclusion, and further evaluation by a doctor is needed.

The conclusion must adhere to the JSON format below:
{"compatibility": "string", "explain": "string"}

For example:
### Medication Information
Medication A: can be used together with B
Medication B: can be used together with A
### List of Medications to Consider
Medication A and Medication B
### Conclusion:
{"compatibility": "RELEVANT", "explain": "Medication B is compatible for use with Medication A"}
"""

COMPATIBLE_TEMPLATE = """
### Medication Information
{drug_info}
### List of Medications to Consider
{drug1} and {drug2}
### Conclusion:
"""

SUMMARIZE_PROMPT = """Your task is to summarize the content of a medical information. 
The summary should only focus on the main section without omitting essential information. 

### Medical Information
{info}
### Summary
"""    