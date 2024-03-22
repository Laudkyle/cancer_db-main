import json
import os

data = {
    "questions": [
       {
      "question": "Name some types of cancer.",
      "answer": "Some types of cancer include breast cancer, lung cancer, prostate cancer, colorectal cancer, leukemia, melanoma, lymphoma, and pancreatic cancer."
    },
    {
      "question": "List a few types of cancer.",
      "answer": "A few types of cancer include breast cancer, lung cancer, prostate cancer, colorectal cancer, leukemia, melanoma, lymphoma, and pancreatic cancer."
    },
    {
      "question": "What are some common types of cancer?",
      "answer": "Common types of cancer include breast cancer, lung cancer, prostate cancer, colorectal cancer, leukemia, melanoma, lymphoma, and pancreatic cancer."
    },
    {
      "question": "Can you name a couple of cancer types?",
      "answer": "Sure, a couple of cancer types are breast cancer, lung cancer, prostate cancer, colorectal cancer, leukemia, melanoma, lymphoma, and pancreatic cancer."
    },
    {
      "question": "What types of cancer are frequently encountered?",
      "answer": "Frequently encountered types of cancer include breast cancer, lung cancer, prostate cancer, colorectal cancer, leukemia, melanoma, lymphoma, and pancreatic cancer."
    },
    {
      "question": "What are the different types of cancer?",
      "answer": "There are numerous types of cancer, including but not limited to breast cancer, lung cancer, prostate cancer, colorectal cancer, skin cancer, and leukemia."
    },
    {
      "question": "Can you name some common types of cancer?",
      "answer": "Common types of cancer include breast cancer, lung cancer, prostate cancer, colorectal cancer, skin cancer, and leukemia."
    },
    {
      "question": "What kinds of cancer are most frequently diagnosed?",
      "answer": "The most frequently diagnosed cancers include breast cancer, lung cancer, prostate cancer, colorectal cancer, skin cancer, and leukemia."
    },
    {
      "question": "Name the types of cancer.",
      "answer": "The types of cancer include breast cancer, lung cancer, prostate cancer, colorectal cancer, leukemia, melanoma, lymphoma, and pancreatic cancer, among others."
    },
    {
      "question": "Can you provide examples of cancer?",
      "answer": "Examples of cancer include breast cancer, lung cancer, prostate cancer, colorectal cancer, leukemia, melanoma, lymphoma, and pancreatic cancer, among others."
    },
    {
      "question": "What are some common examples of cancer?",
      "answer": "Common examples of cancer include breast cancer, lung cancer, prostate cancer, colorectal cancer, leukemia, melanoma, lymphoma, and pancreatic cancer, among others."
    },
    {
      "question": "List some common types of cancer.",
      "answer": "Some common types of cancer include breast cancer, lung cancer, prostate cancer, colorectal cancer, leukemia, melanoma, lymphoma, and pancreatic cancer."
    },
    {
      "question": "What types of cancer are frequently seen?",
      "answer": "Frequently seen types of cancer include breast cancer, lung cancer, prostate cancer, colorectal cancer, leukemia, melanoma, lymphoma, and pancreatic cancer, among others."
    },
    {
      "question": "examples of cancer?",
      "answer": "Examples of cancer include breast cancer, lung cancer, prostate cancer, colorectal cancer, leukemia, melanoma, lymphoma, and pancreatic cancer, among others."
    },
    {
      "question": "some examples of cancer types?",
      "answer": "Examples of cancer types include breast cancer, lung cancer, prostate cancer, colorectal cancer, leukemia, melanoma, lymphoma, and pancreatic cancer, among others."
    },
    {
      "question": "examples of cancer types?",
      "answer": "Examples of cancer types include breast cancer, lung cancer, prostate cancer, colorectal cancer, skin cancer, and leukemia, among others."
    },
    {
      "question": "Name the types of cancer.",
      "answer": "The types of cancer include breast cancer, lung cancer, prostate cancer, colorectal cancer, leukemia, melanoma, lymphoma, and pancreatic cancer."
    },
    {
      "question": "Can you list a few types of cancer?",
      "answer": "A few types of cancer include breast cancer, lung cancer, prostate cancer, colorectal cancer, skin cancer, and leukemia."
    },
    {
      "question": "What are the main categories of cancer?",
      "answer": "The main categories of cancer include carcinoma, sarcoma, leukemia, lymphoma, and central nervous system cancers."
    },{
      "question": "Are there different classifications of cancer?",
      "answer": "Yes, cancer can be classified based on the type of tissue or organ it originates from, its histological characteristics, and its stage of progression."
    },{
      "question": "How many types of cancer are there?",
      "answer": "There are numerous types of cancer, each originating from different tissues and organs in the body."
    },
    {
      "question": "Can you list the various types of cancer?",
      "answer": "Yes, there are many types of cancer, including but not limited to breast cancer, lung cancer, prostate cancer, colorectal cancer, and leukemia."
    },
    {
      "question": "How many different types of cancer exist?",
      "answer": "There are various different types of cancer, each with its own characteristics and origins."
    },
    {
      "question": "What is the total number of cancer types known?",
      "answer": "The total number of known cancer types is continually evolving as research progresses, revealing new subtypes and classifications."
    },
    {
      "question": "How many types of cancer have been identified?",
      "answer": "Numerous types of cancer have been identified, with ongoing research leading to the discovery of new subtypes and classifications."
    },
    {
      "question": "How many types of cancer have been categorized?",
      "answer": "Cancer has been categorized into numerous types based on various factors such as affected organ or tissue."
    },
    {
      "question": "What is the count of known cancer types?",
      "answer": "The count of known cancer types is extensive, encompassing various classifications and subtypes."
    },
    {
      "question": "How many types of cancer are recognized?",
      "answer": "A multitude of cancer types are recognized, each with distinct characteristics and features."
    },
    {
      "question": "What is the total number of cancer categories?",
      "answer": "The total number of cancer categories is substantial, reflecting the diverse nature of the disease."
    },
    {
      "question": "How many types of cancer can occur in the human body?",
      "answer": "Cancer can occur in various types throughout the human body, affecting different organs and tissues."
    },
    {
      "question": "How many distinct cancer types have been documented?",
      "answer": "Numerous distinct cancer types have been documented, with ongoing research shedding light on additional subtypes and variations."
    },
    {
      "question": "What is the total number of cancer varieties?",
      "answer": "The total number of cancer varieties is extensive, reflecting the complexity and diversity of the disease."
    },
    {
      "question": "How many different forms of cancer are known?",
      "answer": "Numerous different forms of cancer are known, each with its own characteristics and behaviors."
    },
    {
      "question": "What is the number of known cancer types?",
      "answer": "The number of known cancer types is continually expanding as research advances and new discoveries are made."
    },
    {
      "question": "How many types of cancer have been classified?",
      "answer": "A large number of cancer types have been classified based on various criteria such as tissue of origin and molecular characteristics."
    },
    {
      "question": "What is the quantity of recognized cancer types?",
      "answer": "The quantity of recognized cancer types is substantial, reflecting the diversity and complexity of the disease."
    },
    {
      "question": "How many types of cancer are documented?",
      "answer": "Numerous types of cancer are documented, each with its own set of characteristics and manifestations."
    },
    {
      "question": "What is the total number of cancer classifications?",
      "answer": "The total number of cancer classifications is significant, reflecting the diverse nature of the disease and its manifestations."
    },
    {
      "question": "How many categories of cancer are recognized?",
      "answer": "Numerous categories of cancer are recognized, each encompassing various types and subtypes."
    },
    {
      "question": "What is the total number of cancer forms identified?",
      "answer": "The total number of cancer forms identified is extensive, reflecting the broad spectrum of the disease."
    },
    {
      "question": "Please provide information on types of cancer.",
      "answer": "Certainly! There are numerous types of cancer, each originating from different tissues and organs in the body."
    },
    {
      "question": "Could you elaborate on the different types of cancer?",
      "answer": "Of course! Cancer encompasses various types, including but not limited to breast cancer, lung cancer, prostate cancer, colorectal cancer, and leukemia."
    },
    {
      "question": "I'd like to learn about the different types of cancer.",
      "answer": "Certainly! Cancer presents in many different forms, each with its own characteristics and origins."
    },
    {
      "question": "Could you provide details on the known types of cancer?",
      "answer": "Absolutely! There are numerous types of cancer known to medical science, with ongoing research uncovering new subtypes and classifications."
    },
    {
      "question": "I'm interested in understanding the variety of cancer types.",
      "answer": "Certainly! Cancer manifests in numerous types, with ongoing research leading to the discovery of new subtypes and classifications."
    },
    {
      "question": "Can you tell me more about the classifications of cancer?",
      "answer": "Of course! Cancer is classified into numerous types based on various factors such as affected organ or tissue."
    },
    {
      "question": "Please elaborate on the categorization of cancer.",
      "answer": "Certainly! Cancer has been categorized into numerous types based on various factors such as tissue of origin and molecular characteristics."
    },
    {
      "question": "Could you shed some light on the types of cancer recognized by medical science?",
      "answer": "Absolutely! A multitude of cancer types are recognized, each with distinct characteristics and features."
    },
    {
      "question": "I'd like to gain insight into the recognized cancer types.",
      "answer": "Of course! There are numerous recognized cancer types, each with its own set of characteristics and manifestations."
    },
    {
      "question": "Can you provide an overview of cancer types documented in medical literature?",
      "answer": "Certainly! Numerous types of cancer are documented in medical literature, each with its own set of characteristics and manifestations."
    },
    {
      "question": "I'm curious about the various forms of cancer known to science.",
      "answer": "Absolutely! There are numerous different forms of cancer known to science, each with its own set of characteristics and behaviors."
    },
    {
      "question": "Can you give me a brief overview of the different forms of cancer?",
      "answer": "Of course! Cancer presents in various forms, with each form exhibiting unique characteristics and behaviors."
    },
    {
      "question": "I'd like to know more about the different classifications of cancer.",
      "answer": "Certainly! Cancer has been classified into various types based on factors such as tissue of origin and cellular characteristics."
    },
    {
      "question": "Can you provide an overview of the classifications of cancer?",
      "answer": "Absolutely! Cancer is classified into various types based on factors such as affected organ or tissue."
    },
    {
      "question": "Please provide an overview of the categories of cancer.",
      "answer": "Of course! Cancer is categorized into various types based on factors such as tissue of origin and molecular characteristics."
    },
    {
      "question": "I'd like to learn more about the different categories of cancer.",
      "answer": "Certainly! Cancer is categorized into various types based on factors such as affected organ or tissue."
    },
    {
      "question": "Can you provide an overview of the forms of cancer recognized by medical science?",
      "answer": "Absolutely! There are numerous forms of cancer recognized by medical science, each with distinct characteristics and features."
    },
    {
      "question": "I'd like to gain insight into the recognized forms of cancer.",
      "answer": "Of course! There are numerous recognized forms of cancer, each with distinct characteristics and features."
    },
    {
      "question": "Can you provide an overview of the types of cancer documented in medical literature?",
      "answer": "Certainly! Numerous types of cancer are documented in medical literature, each with distinct characteristics and features."
    },
    {
      "question": "I'm curious about the various categories of cancer known to science.",
      "answer": "Absolutely! There are numerous categories of cancer known to science, each encompassing various types and subtypes."
    },
    {
      "question": "Cancer types?",
      "answer": "Cancer is a complex disease characterized by the uncontrolled growth and spread of abnormal cells in the body. There are numerous types of cancer, each originating from different tissues and organs. These include but are not limited to breast cancer, lung cancer, prostate cancer, colorectal cancer, leukemia, melanoma, lymphoma, and pancreatic cancer. Each type of cancer has its own set of characteristics, symptoms, and treatments, making it essential for individuals to undergo proper diagnosis and management under the guidance of healthcare professionals."
    },
    {
      "question": "Cancer varieties?",
      "answer": "Cancer encompasses a wide range of varieties, with each type affecting different tissues and organs in the body. These varieties include but are not limited to carcinoma, sarcoma, lymphoma, leukemia, and melanoma. Carcinomas arise from epithelial cells and are the most common type of cancer. Sarcomas originate from connective tissues such as bone, cartilage, or muscle. Lymphomas affect the lymphatic system, while leukemias involve the blood and bone marrow. Melanomas arise from pigment-producing cells called melanocytes. Understanding the various cancer varieties is crucial for accurate diagnosis and treatment planning."
    },
    {
      "question": "Types?",
      "answer": "Cancer comes in various types, each originating from different tissues and organs in the body. These types include but are not limited to carcinomas, sarcomas, lymphomas, leukemias, and melanomas. Carcinomas are the most common type of cancer, arising from epithelial cells that line organs and tissues. Sarcomas originate from connective tissues such as bone, cartilage, or muscle. Lymphomas affect the lymphatic system, while leukemias involve the blood and bone marrow. Melanomas arise from pigment-producing cells called melanocytes. Understanding the different types of cancer is essential for accurate diagnosis and appropriate treatment selection."
    },
    {
      "question": "Varieties?",
      "answer": "There are numerous varieties of cancer, each with distinct characteristics and behaviors. These varieties encompass a wide range of cancer types, including carcinomas, sarcomas, lymphomas, leukemias, and melanomas. Carcinomas, which arise from epithelial cells, account for the majority of cancer cases and can affect various organs and tissues in the body. Sarcomas originate from connective tissues such as bone, cartilage, or muscle. Lymphomas affect the lymphatic system, while leukemias involve the blood and bone marrow. Melanomas arise from pigment-producing cells called melanocytes. Each cancer variety requires specific diagnostic approaches and treatment strategies tailored to its unique features."
    },
    {
      "question": "Cancer categories?",
      "answer": "Cancer has been categorized into numerous types based on factors such as tissue of origin, histological characteristics, and molecular profiles. These categories encompass a broad range of cancer types, including but not limited to carcinomas, sarcomas, lymphomas, leukemias, and melanomas. Carcinomas arise from epithelial cells lining organs and tissues and are the most common type of cancer. Sarcomas originate from connective tissues such as bone, cartilage, or muscle. Lymphomas affect the lymphatic system, while leukemias involve the blood and bone marrow. Melanomas arise from pigment-producing cells called melanocytes. Understanding cancer categories is essential for accurate diagnosis, prognosis, and treatment planning."
    },
    {
      "question": "Categories?",
      "answer": "There are many categories of cancer, each encompassing various types and subtypes based on factors such as tissue of origin, histological features, and genetic alterations. These categories include but are not limited to carcinomas, sarcomas, lymphomas, leukemias, and melanomas. Carcinomas arise from epithelial cells lining organs and tissues and represent the most common type of cancer. Sarcomas originate from connective tissues such as bone, cartilage, or muscle. Lymphomas affect the lymphatic system, while leukemias involve the blood and bone marrow. Melanomas arise from pigment-producing cells called melanocytes. Each category of cancer requires specific diagnostic and therapeutic approaches tailored to its unique characteristics."
    },
    {
      "question": "Different forms?",
      "answer": "Cancer manifests in various forms, with each type exhibiting distinct characteristics and behaviors. These forms encompass a wide range of cancer types, including carcinomas, sarcomas, lymphomas, leukemias, and melanomas. Carcinomas arise from epithelial cells lining organs and tissues and represent the most prevalent form of cancer. Sarcomas originate from connective tissues such as bone, cartilage, or muscle. Lymphomas affect the lymphatic system, while leukemias involve the blood and bone marrow. Melanomas arise from pigment-producing cells called melanocytes. Understanding the different forms of cancer is crucial for accurate diagnosis and personalized treatment planning."
    },
    ]
}

intents = {
    "intents": [
        {
            "tag": "what are the types of cancer?",
            "patterns": [q["question"] for q in data["questions"]],
            "responses": [q["answer"] for q in data["questions"]]
        }
    ]
}

# Define the file path
file_path = "intents.json"

# Check if the file exists
if os.path.exists(file_path):
    # Load existing data from the file
    with open(file_path, "r") as infile:
        existing_data = json.load(infile)
    
    # Append the new data to the existing data
    existing_data["intents"].extend(intents["intents"])
    
    # Write the combined data back to the file
    with open(file_path, "w") as outfile:
        json.dump(existing_data, outfile, indent=4)
else:
    # If the file doesn't exist, create a new one with the combined data
    with open(file_path, "w") as outfile:
        json.dump(intents, outfile, indent=4)

print(f"Data combined and appended to '{file_path}'.")
