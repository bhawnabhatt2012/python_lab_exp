#line1 = input('Enter the first word: ')
#line2 = input('Enter the second word: ')

import cgi

def anagrams(s1,s2):
    def sort(s):
        return sorted(s.lower().strip())
    return sort(s1)==sort(s2)

form = cgi.FieldStorage()
#print(anagrams(line1,line2))
print ("Content-type:text/html\r\n\r\n")
print('<html>')
print('<head>')
print('<title>Is this word an anagram?</title>')
print('</head>')
print('<body>')
print('<form>')
print('String 1: <input type="text" name ="string1"/> ')
print('String 2: <input type="text" name="string2" />')
print('<input type="submit" name="check_btn" value="Check">')
if(form.getvalue('string1') and form.getvalue('string2')):
    first_string = form.getvalue('string1')
    second_string = form.getvalue('string2')
    result = anagrams(first_string,second_string)
    if result == True:
        print('<h3>The word is an anagram</h3>')
    else:
        print('<h3>The word is not an anagram</h3>')
print('</form>')
print('</body>')
print('</html>')