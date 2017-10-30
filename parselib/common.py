
def test_resource_extractor(extractor, filename):
    result = extractor.get_resource(filename)

    print("Title: [{0}]".format(result["article_title"]))
    print("Author: [{0}]".format(", ".join([a["article_author_name"] for a in result["article_author"]])))
    print("Time: [{0}]".format(result["article_time"]))
    print("Source: [{0}]".format(result["article_source"]))
    print("Text: [{0}]".format(result["article_text"]))
    print("Comments: {0}".format(len(result["comments"])))
    print("Root Comments: {0}".format(len([c for c in result["comments"] if "comment_replyTo" not in c])))
    print()
