#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This function turns numerical inputs into english text

EXAMPLE

input:
1234567 

gives output:
one million, two hundred and thirty four thousand, five hundred and sixty seven 

Known issues:
* some numbers produce conbinations of commas and 'ands' that are not quite right


"""

def integertotext (input):

# Define text lists

    ones = ('', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')
    tens = ('','ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety')
    teens = ('', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen')
    thousandpowers = ('', 'thousand', 'million', 'billion', 'trillion')

# Define maximum value

    maxpermissiblevalue = 999999999999999

# Get input

    inputnumber = input

# Check input is within current deliverable parameters

    try:
        val = int(inputnumber)

    except ValueError:
        print('input string must be an integer')
        return
    
    if (val > maxpermissiblevalue):
        print('Sorry, I can only handle numbers up to', maxpermissiblevalue)
        return
    
    checkednumber = int(inputnumber)
    
# split into unit counts as COUNTLIST

    countlist = []

    for i in range (0,len(str(checkednumber))):
    
        countlist.append(int(checkednumber%10))
        checkednumber = (checkednumber - (checkednumber%10))/10

# iterate per thousand block

    outputtext = str()
    
    for thousandindex in range (0,len(countlist),3):
            
        thousandtext = str()

        extendedcountlist = countlist + [0, 0]
        needand = False
        needones = False
        needtens = False
            
        if  len(countlist) >= thousandindex and extendedcountlist[thousandindex] != 0:
            
            needones = True
            thousandtext =  str(ones[extendedcountlist[thousandindex]])
            
        if  len(countlist) >= thousandindex+1 and extendedcountlist[thousandindex+1] != 0:

            needtens = True
            thousandtext =  str(tens[extendedcountlist[thousandindex+1]]) + ' ' + thousandtext 

# shuffling the 'and'
            
        if needones or needtens: needand = True
        
        if len(countlist) < thousandindex+3: needand = False
    
        if needand: thousandtext = ' and ' + thousandtext 
    
        if  len(countlist) >= thousandindex+2 and extendedcountlist[thousandindex+2] != 0:
        
            thousandtext =  str(ones[extendedcountlist[thousandindex+2]]) + ' hundred' + thousandtext
   
        thousandpowersindex = int((thousandindex-thousandindex%3)/3)
        
        if thousandtext != '': thousandtext = thousandtext + ' ' + str(thousandpowers[thousandpowersindex])
    
        if thousandtext != '': outputtext = thousandtext + ', ' + outputtext
    
# fix the teens

    for index in range (1,10):
        outputtext = outputtext.replace( str(tens[1] + ' ' + ones[index]), str(teens[index]) )

# remove any double spaces 

    outputtext = outputtext.replace('  ', ' ')

# remove comma in 1001-1099, 1001001 etc
    
    for j in range (0, len(thousandpowers)):

        outputtext = outputtext.replace( str(thousandpowers[j]) + ', and', str(thousandpowers[j]) +' and')

# make 0 mean zero (with two extra spaces to account for my bad code)
 
    if outputtext == '': outputtext = 'zero  '

# remove extraneous characters at the end
    
    for i in range (len(outputtext)-1, len(outputtext)-3, -1):
     
            if outputtext[i] == ',' or ' ': 
                outputtext = outputtext[:i]

# Display output

    print (outputtext)


    
    
