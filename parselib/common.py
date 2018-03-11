
def test_resource_extractor(extractor, filename):
    result = extractor.get_resource(filename)

    print("Lecture: [{0}]".format(result["lecture_title"]))
    print("Semester: [{0}]".format(result["semester"]))
    #print("Text: [{0}]".format(result["article_text"]))
    #print("Comments: {0}".format(len(result["comments"])))
    #print("Root Comments: {0}".format(len([c for c in result["comments"] if "comment_replyTo" not in c])))
    print()
