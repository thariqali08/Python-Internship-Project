import difflib

#Calculate the similarity between input docs and database docs
def calc_simi(doc1,doc2):

    #Calculate similarity ratio using SequenceMatcher
    similarity=difflib.SequenceMatcher(None,doc1,doc2).ratio()


    return similarity

#Detect the plagiarism of input documents
def plagiarism_detector(input_doc,database_docs,threshold=0.7):
    plagiarized_doc=[]

    for doc in database_docs:

        similarity = calc_simi(input_doc,doc)
        if similarity >= threshold:
            plag_ratio=similarity*100
            print("Plagiarism Detecting ratio in %: ""{:.2f}".format(plag_ratio))
            plagiarized_doc.append(doc)

    return plagiarized_doc
        

if __name__== '__main__':

    #This is database documents
    database_docs=[
        "Scientists and researchers utilize technology in various fields,such as genetics, space exploration,nanotechnology etc.",
        "Technology plays a significant role in social networking, activism, humanitarian efforts,fostering collaborations and empowering communities.",
        "Technology is used in classrooms to enhance learning through digital resources, online courses, educational apps.",
        " Science generates knowledge through systematic observation, experimentation, and analysis. ",
        " Science contributes to the study of the environment, climate change, biodiversity, and sustainability.",
        " Python is widely used in data analysis and visualization. Libraries such as NumPy, Pandas, and Matplotlib."
    ]

    #Get the input documents from user   
    input_doc=str(input("Enter the Paragraph:"))

    plagiarized_docs=plagiarism_detector(input_doc,database_docs)

    if plagiarized_docs:
        print("Plagiarized Documents:")
        for doc in plagiarized_docs:
            print(doc)

    else:
        print("No Plagiarism Detected.")        