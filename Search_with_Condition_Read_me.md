field_name1__startswith  if field is character and start with character ''
field_name1__endswith  if field is character and ends with character ''

gte refer to greater than or equal
lte refer to less than or equal
gt greater than
lt  less than 

the field "seperation" ether value '|' or '&'

{

{
"field_name1__startswith":'ll',
"field_name2__endswith":'kk',
"fieldname3":'nn',
"field_name4__gte":'gte',
"field_name5__lte":'cd',
"field_name5__lt":'cv',
"field_name5__gt":'vb',
}]
,
"sep":"1"

}



example  where sep =1 is and where sep=2 is or 

{

"Journey_type": 1,
            "stat": 4

,
"sep":"1"

}
