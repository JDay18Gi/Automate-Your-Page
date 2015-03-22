#Unfortunately, my html was not written as to be as automatable as Andy's was.

def generate_concept_HTML(concept_title, concept_description):
    html_text_1 = '''
		    <p>
		   		<h3>''' + concept_title
    html_text_2 = '''</h3>
		   		<p>''' + concept_description
    html_text_3 = '''</p>
		    <br>'''
    
    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text


def make_HTML(concept):  
    concept_title = concept[0]
    concept_description = concept[1]
    return generate_concept_HTML(concept_title, concept_description)

LIST_OF_CONCEPTS = [ ['Variables', 'Variables can be assigned any meaning we want. They can be assigned the meaning of numbers, lists of numbers, formulas, words, phrases, even huge pages of text or code.  Variables conveniently allow long complex statements to be contained in just a word or letter.'],
                             ['For Loop', 'Strings are characters surrounded by quotes. Strings can be added together but they cannot be added to numbers.'] ]

def make_HTML_for_many_concepts(list_of_concepts):
    HTML = ""
    for concept in list_of_concepts:
        concept_HTML = make_HTML(concept)
        HTML = HTML + concept_HTML
    return HTML

print make_HTML_for_many_concepts(LIST_OF_CONCEPTS)
