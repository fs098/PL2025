
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "AND ARRAY ASSIGN BEGIN BOOLEAN CHAR CONST DIV DO DOWNTO ELSE END FALSE FOR IF INTEGER LARGEREQUALS MINOREQUALS MOD NOT NOTEQUAL OF OR PROGRAM REAL STRING THEN TO TRUE TWODOTS VAR WHILE comment id num textprogram : PROGRAM id ';' declarations block '.' block : BEGIN statements END terminatordeclarations : VAR declaration_list ';' \n                    | CONST declaration_list ';' \n                    | VAR declaration_list  CONST declaration_list  \n                    | CONST declaration_list  VAR declaration_list \n                    | declaration_list : declaration\n                        | declaration_list ';' declarationdeclaration : id_list ':' typeid_list : id\n               | id_list ',' idtype : INTEGER\n            | REAL\n            | STRING\n            | CHAR\n            | BOOLEAN\n            | ARRAY '[' expression ']' OF typestatements : statement \n                  | statements statement statement : block\n                 | assignment\n                 | if_statement\n                 | while_statement\n                 | for_statement\n                 | comments\n                 | function_callassignment : id ASSIGN expressionif_statement : IF exprBool THEN statement ifContifCont : \n              | ELSE statementwhile_statement : WHILE expression DO statementfor_statement : FOR id ASSIGN expression forContforCont : TO expression DO statement\n                | DOWNTO expression DO statementexprBool : expression\n                | expression opRel expression\n                | NOT expressionopRel : '=' \n             | NOTEQUAL\n             | '<'\n             | '>'\n             | MINOREQUALS\n             | LARGEREQUALS expression : term\n                  | expression opAdd term\n                  | num TWODOTS numopAdd : '+'\n             | '-'\n             | ORterm : factor\n             | term opMul factoropMul : '*'\n             | '/'\n             | '%'\n             | AND\n             | MOD\n             | DIVfactor : const terminator\n              | var terminator\n              | function_call\n              | '(' exprBool ')' const : num\n             | text\n             | TRUE\n             | FALSEvar : id\n           | id '[' expression ']' function_call : id '(' ')' terminator\n                     | id '(' arg_list ')' terminatorterminator : ';'\n                  | arg_list : expression\n                | arg_list ',' expressioncomments : comment"
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,15,],[0,-1,]),'id':([2,6,7,9,16,17,18,19,20,21,22,23,24,26,27,28,29,30,31,33,34,35,36,37,38,39,42,43,44,45,46,47,48,49,50,51,52,53,67,68,69,70,73,74,75,76,77,78,79,80,81,82,83,84,86,87,88,89,90,91,92,94,95,97,98,99,100,101,102,103,104,105,107,108,109,110,111,113,116,118,119,120,121,122,123,125,129,130,132,133,],[3,13,13,25,25,-19,-21,-22,-23,-24,-25,-26,-27,53,53,55,-75,13,13,65,13,13,-72,-20,53,53,53,-45,-63,-51,-72,-72,-61,53,-64,-65,-66,-67,-2,-71,-28,-72,25,53,53,-39,-40,-41,-42,-43,-44,-48,-49,-50,53,-53,-54,-55,-56,-57,-58,-59,-60,53,25,53,13,53,-69,-72,53,-30,-46,-63,-52,-47,-62,-32,-70,-29,25,-68,-33,53,53,-31,25,25,-34,-35,]),';':([3,10,11,14,36,44,46,47,50,51,52,53,56,57,58,59,60,61,62,63,66,70,103,108,120,131,],[4,30,-8,34,68,-63,68,68,-64,-65,-66,-67,-9,100,-10,-13,-14,-15,-16,-17,100,68,68,-63,-68,-18,]),'VAR':([4,11,14,56,58,59,60,61,62,63,131,],[6,-8,35,-9,-10,-13,-14,-15,-16,-17,-18,]),'CONST':([4,10,11,56,58,59,60,61,62,63,131,],[7,31,-8,-9,-10,-13,-14,-15,-16,-17,-18,]),'BEGIN':([4,5,9,11,16,17,18,19,20,21,22,23,24,29,30,34,36,37,43,44,45,46,47,48,50,51,52,53,56,57,58,59,60,61,62,63,66,67,68,69,70,73,94,95,98,102,103,105,107,108,109,110,111,113,116,118,119,120,121,125,129,130,131,132,133,],[-7,9,9,-8,9,-19,-21,-22,-23,-24,-25,-26,-27,-75,-3,-4,-72,-20,-45,-63,-51,-72,-72,-61,-64,-65,-66,-67,-9,-5,-10,-13,-14,-15,-16,-17,-6,-2,-71,-28,-72,9,-59,-60,9,-69,-72,-30,-46,-63,-52,-47,-62,-32,-70,-29,9,-68,-33,-31,9,9,-18,-34,-35,]),'.':([8,36,67,68,],[15,-72,-2,-71,]),'IF':([9,16,17,18,19,20,21,22,23,24,29,36,37,43,44,45,46,47,48,50,51,52,53,67,68,69,70,73,94,95,98,102,103,105,107,108,109,110,111,113,116,118,119,120,121,125,129,130,132,133,],[26,26,-19,-21,-22,-23,-24,-25,-26,-27,-75,-72,-20,-45,-63,-51,-72,-72,-61,-64,-65,-66,-67,-2,-71,-28,-72,26,-59,-60,26,-69,-72,-30,-46,-63,-52,-47,-62,-32,-70,-29,26,-68,-33,-31,26,26,-34,-35,]),'WHILE':([9,16,17,18,19,20,21,22,23,24,29,36,37,43,44,45,46,47,48,50,51,52,53,67,68,69,70,73,94,95,98,102,103,105,107,108,109,110,111,113,116,118,119,120,121,125,129,130,132,133,],[27,27,-19,-21,-22,-23,-24,-25,-26,-27,-75,-72,-20,-45,-63,-51,-72,-72,-61,-64,-65,-66,-67,-2,-71,-28,-72,27,-59,-60,27,-69,-72,-30,-46,-63,-52,-47,-62,-32,-70,-29,27,-68,-33,-31,27,27,-34,-35,]),'FOR':([9,16,17,18,19,20,21,22,23,24,29,36,37,43,44,45,46,47,48,50,51,52,53,67,68,69,70,73,94,95,98,102,103,105,107,108,109,110,111,113,116,118,119,120,121,125,129,130,132,133,],[28,28,-19,-21,-22,-23,-24,-25,-26,-27,-75,-72,-20,-45,-63,-51,-72,-72,-61,-64,-65,-66,-67,-2,-71,-28,-72,28,-59,-60,28,-69,-72,-30,-46,-63,-52,-47,-62,-32,-70,-29,28,-68,-33,-31,28,28,-34,-35,]),'comment':([9,16,17,18,19,20,21,22,23,24,29,36,37,43,44,45,46,47,48,50,51,52,53,67,68,69,70,73,94,95,98,102,103,105,107,108,109,110,111,113,116,118,119,120,121,125,129,130,132,133,],[29,29,-19,-21,-22,-23,-24,-25,-26,-27,-75,-72,-20,-45,-63,-51,-72,-72,-61,-64,-65,-66,-67,-2,-71,-28,-72,29,-59,-60,29,-69,-72,-30,-46,-63,-52,-47,-62,-32,-70,-29,29,-68,-33,-31,29,29,-34,-35,]),':':([12,13,65,],[32,-11,-12,]),',':([12,13,43,44,45,46,47,48,50,51,52,53,65,68,70,71,72,94,95,102,103,107,108,109,110,111,116,117,120,],[33,-11,-45,-63,-51,-72,-72,-61,-64,-65,-66,-67,-12,-71,-72,104,-73,-59,-60,-69,-72,-46,-63,-52,-47,-62,-70,-74,-68,]),'END':([16,17,18,19,20,21,22,23,24,29,36,37,43,44,45,46,47,48,50,51,52,53,67,68,69,70,94,95,102,103,105,107,108,109,110,111,113,116,118,120,121,125,132,133,],[36,-19,-21,-22,-23,-24,-25,-26,-27,-75,-72,-20,-45,-63,-51,-72,-72,-61,-64,-65,-66,-67,-2,-71,-28,-72,-59,-60,-69,-72,-30,-46,-63,-52,-47,-62,-32,-70,-29,-68,-33,-31,-34,-35,]),'ELSE':([18,19,20,21,22,23,24,29,36,43,44,45,46,47,48,50,51,52,53,67,68,69,70,94,95,102,103,105,107,108,109,110,111,113,116,118,120,121,125,132,133,],[-21,-22,-23,-24,-25,-26,-27,-75,-72,-45,-63,-51,-72,-72,-61,-64,-65,-66,-67,-2,-71,-28,-72,-59,-60,-69,-72,119,-46,-63,-52,-47,-62,-32,-70,-29,-68,-33,-31,-34,-35,]),'ASSIGN':([25,55,],[38,99,]),'(':([25,26,27,38,39,42,49,53,74,75,76,77,78,79,80,81,82,83,84,86,87,88,89,90,91,92,97,99,101,104,122,123,],[39,49,49,49,49,49,49,39,49,49,-39,-40,-41,-42,-43,-44,-48,-49,-50,49,-53,-54,-55,-56,-57,-58,49,49,49,49,49,49,]),'NOT':([26,49,],[42,42,]),'num':([26,27,38,39,42,49,74,75,76,77,78,79,80,81,82,83,84,86,87,88,89,90,91,92,93,97,99,101,104,122,123,],[44,44,44,44,44,44,44,108,-39,-40,-41,-42,-43,-44,-48,-49,-50,108,-53,-54,-55,-56,-57,-58,110,44,44,44,44,44,44,]),'text':([26,27,38,39,42,49,74,75,76,77,78,79,80,81,82,83,84,86,87,88,89,90,91,92,97,99,101,104,122,123,],[50,50,50,50,50,50,50,50,-39,-40,-41,-42,-43,-44,-48,-49,-50,50,-53,-54,-55,-56,-57,-58,50,50,50,50,50,50,]),'TRUE':([26,27,38,39,42,49,74,75,76,77,78,79,80,81,82,83,84,86,87,88,89,90,91,92,97,99,101,104,122,123,],[51,51,51,51,51,51,51,51,-39,-40,-41,-42,-43,-44,-48,-49,-50,51,-53,-54,-55,-56,-57,-58,51,51,51,51,51,51,]),'FALSE':([26,27,38,39,42,49,74,75,76,77,78,79,80,81,82,83,84,86,87,88,89,90,91,92,97,99,101,104,122,123,],[52,52,52,52,52,52,52,52,-39,-40,-41,-42,-43,-44,-48,-49,-50,52,-53,-54,-55,-56,-57,-58,52,52,52,52,52,52,]),'INTEGER':([32,128,],[59,59,]),'REAL':([32,128,],[60,60,]),'STRING':([32,128,],[61,61,]),'CHAR':([32,128,],[62,62,]),'BOOLEAN':([32,128,],[63,63,]),'ARRAY':([32,128,],[64,64,]),')':([39,41,43,44,45,46,47,48,50,51,52,53,68,70,71,72,85,94,95,96,102,103,106,107,108,109,110,111,116,117,120,],[70,-36,-45,-63,-51,-72,-72,-61,-64,-65,-66,-67,-71,-72,103,-73,-38,-59,-60,111,-69,-72,-37,-46,-63,-52,-47,-62,-70,-74,-68,]),'THEN':([40,41,43,44,45,46,47,48,50,51,52,53,68,70,85,94,95,102,103,106,107,108,109,110,111,116,120,],[73,-36,-45,-63,-51,-72,-72,-61,-64,-65,-66,-67,-71,-72,-38,-59,-60,-69,-72,-37,-46,-63,-52,-47,-62,-70,-68,]),'=':([41,43,44,45,46,47,48,50,51,52,53,68,70,94,95,102,103,107,108,109,110,111,116,120,],[76,-45,-63,-51,-72,-72,-61,-64,-65,-66,-67,-71,-72,-59,-60,-69,-72,-46,-63,-52,-47,-62,-70,-68,]),'NOTEQUAL':([41,43,44,45,46,47,48,50,51,52,53,68,70,94,95,102,103,107,108,109,110,111,116,120,],[77,-45,-63,-51,-72,-72,-61,-64,-65,-66,-67,-71,-72,-59,-60,-69,-72,-46,-63,-52,-47,-62,-70,-68,]),'<':([41,43,44,45,46,47,48,50,51,52,53,68,70,94,95,102,103,107,108,109,110,111,116,120,],[78,-45,-63,-51,-72,-72,-61,-64,-65,-66,-67,-71,-72,-59,-60,-69,-72,-46,-63,-52,-47,-62,-70,-68,]),'>':([41,43,44,45,46,47,48,50,51,52,53,68,70,94,95,102,103,107,108,109,110,111,116,120,],[79,-45,-63,-51,-72,-72,-61,-64,-65,-66,-67,-71,-72,-59,-60,-69,-72,-46,-63,-52,-47,-62,-70,-68,]),'MINOREQUALS':([41,43,44,45,46,47,48,50,51,52,53,68,70,94,95,102,103,107,108,109,110,111,116,120,],[80,-45,-63,-51,-72,-72,-61,-64,-65,-66,-67,-71,-72,-59,-60,-69,-72,-46,-63,-52,-47,-62,-70,-68,]),'LARGEREQUALS':([41,43,44,45,46,47,48,50,51,52,53,68,70,94,95,102,103,107,108,109,110,111,116,120,],[81,-45,-63,-51,-72,-72,-61,-64,-65,-66,-67,-71,-72,-59,-60,-69,-72,-46,-63,-52,-47,-62,-70,-68,]),'+':([41,43,44,45,46,47,48,50,51,52,53,54,68,69,70,72,85,94,95,102,103,106,107,108,109,110,111,112,114,115,116,117,120,126,127,],[82,-45,-63,-51,-72,-72,-61,-64,-65,-66,-67,82,-71,82,-72,82,82,-59,-60,-69,-72,82,-46,-63,-52,-47,-62,82,82,82,-70,82,-68,82,82,]),'-':([41,43,44,45,46,47,48,50,51,52,53,54,68,69,70,72,85,94,95,102,103,106,107,108,109,110,111,112,114,115,116,117,120,126,127,],[83,-45,-63,-51,-72,-72,-61,-64,-65,-66,-67,83,-71,83,-72,83,83,-59,-60,-69,-72,83,-46,-63,-52,-47,-62,83,83,83,-70,83,-68,83,83,]),'OR':([41,43,44,45,46,47,48,50,51,52,53,54,68,69,70,72,85,94,95,102,103,106,107,108,109,110,111,112,114,115,116,117,120,126,127,],[84,-45,-63,-51,-72,-72,-61,-64,-65,-66,-67,84,-71,84,-72,84,84,-59,-60,-69,-72,84,-46,-63,-52,-47,-62,84,84,84,-70,84,-68,84,84,]),'DO':([43,44,45,46,47,48,50,51,52,53,54,68,70,94,95,102,103,107,108,109,110,111,116,120,126,127,],[-45,-63,-51,-72,-72,-61,-64,-65,-66,-67,98,-71,-72,-59,-60,-69,-72,-46,-63,-52,-47,-62,-70,-68,129,130,]),']':([43,44,45,46,47,48,50,51,52,53,68,70,94,95,102,103,107,108,109,110,111,112,115,116,120,],[-45,-63,-51,-72,-72,-61,-64,-65,-66,-67,-71,-72,-59,-60,-69,-72,-46,-63,-52,-47,-62,120,124,-70,-68,]),'TO':([43,44,45,46,47,48,50,51,52,53,68,70,94,95,102,103,107,108,109,110,111,114,116,120,],[-45,-63,-51,-72,-72,-61,-64,-65,-66,-67,-71,-72,-59,-60,-69,-72,-46,-63,-52,-47,-62,122,-70,-68,]),'DOWNTO':([43,44,45,46,47,48,50,51,52,53,68,70,94,95,102,103,107,108,109,110,111,114,116,120,],[-45,-63,-51,-72,-72,-61,-64,-65,-66,-67,-71,-72,-59,-60,-69,-72,-46,-63,-52,-47,-62,123,-70,-68,]),'*':([43,44,45,46,47,48,50,51,52,53,68,70,94,95,102,103,107,108,109,111,116,120,],[87,-63,-51,-72,-72,-61,-64,-65,-66,-67,-71,-72,-59,-60,-69,-72,87,-63,-52,-62,-70,-68,]),'/':([43,44,45,46,47,48,50,51,52,53,68,70,94,95,102,103,107,108,109,111,116,120,],[88,-63,-51,-72,-72,-61,-64,-65,-66,-67,-71,-72,-59,-60,-69,-72,88,-63,-52,-62,-70,-68,]),'%':([43,44,45,46,47,48,50,51,52,53,68,70,94,95,102,103,107,108,109,111,116,120,],[89,-63,-51,-72,-72,-61,-64,-65,-66,-67,-71,-72,-59,-60,-69,-72,89,-63,-52,-62,-70,-68,]),'AND':([43,44,45,46,47,48,50,51,52,53,68,70,94,95,102,103,107,108,109,111,116,120,],[90,-63,-51,-72,-72,-61,-64,-65,-66,-67,-71,-72,-59,-60,-69,-72,90,-63,-52,-62,-70,-68,]),'MOD':([43,44,45,46,47,48,50,51,52,53,68,70,94,95,102,103,107,108,109,111,116,120,],[91,-63,-51,-72,-72,-61,-64,-65,-66,-67,-71,-72,-59,-60,-69,-72,91,-63,-52,-62,-70,-68,]),'DIV':([43,44,45,46,47,48,50,51,52,53,68,70,94,95,102,103,107,108,109,111,116,120,],[92,-63,-51,-72,-72,-61,-64,-65,-66,-67,-71,-72,-59,-60,-69,-72,92,-63,-52,-62,-70,-68,]),'TWODOTS':([44,],[93,]),'[':([53,64,],[97,101,]),'OF':([124,],[128,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'declarations':([4,],[5,]),'block':([5,9,16,73,98,119,129,130,],[8,18,18,18,18,18,18,18,]),'declaration_list':([6,7,31,35,],[10,14,57,66,]),'declaration':([6,7,30,31,34,35,100,],[11,11,56,11,56,11,56,]),'id_list':([6,7,30,31,34,35,100,],[12,12,12,12,12,12,12,]),'statements':([9,],[16,]),'statement':([9,16,73,98,119,129,130,],[17,37,105,113,125,132,133,]),'assignment':([9,16,73,98,119,129,130,],[19,19,19,19,19,19,19,]),'if_statement':([9,16,73,98,119,129,130,],[20,20,20,20,20,20,20,]),'while_statement':([9,16,73,98,119,129,130,],[21,21,21,21,21,21,21,]),'for_statement':([9,16,73,98,119,129,130,],[22,22,22,22,22,22,22,]),'comments':([9,16,73,98,119,129,130,],[23,23,23,23,23,23,23,]),'function_call':([9,16,26,27,38,39,42,49,73,74,75,86,97,98,99,101,104,119,122,123,129,130,],[24,24,48,48,48,48,48,48,24,48,48,48,48,24,48,48,48,24,48,48,24,24,]),'exprBool':([26,49,],[40,96,]),'expression':([26,27,38,39,42,49,74,97,99,101,104,122,123,],[41,54,69,72,85,41,106,112,114,115,117,126,127,]),'term':([26,27,38,39,42,49,74,75,97,99,101,104,122,123,],[43,43,43,43,43,43,43,107,43,43,43,43,43,43,]),'factor':([26,27,38,39,42,49,74,75,86,97,99,101,104,122,123,],[45,45,45,45,45,45,45,45,109,45,45,45,45,45,45,]),'const':([26,27,38,39,42,49,74,75,86,97,99,101,104,122,123,],[46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,]),'var':([26,27,38,39,42,49,74,75,86,97,99,101,104,122,123,],[47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,]),'type':([32,128,],[58,131,]),'terminator':([36,46,47,70,103,],[67,94,95,102,116,]),'arg_list':([39,],[71,]),'opRel':([41,],[74,]),'opAdd':([41,54,69,72,85,106,112,114,115,117,126,127,],[75,75,75,75,75,75,75,75,75,75,75,75,]),'opMul':([43,107,],[86,86,]),'ifCont':([105,],[118,]),'forCont':([114,],[121,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROGRAM id ; declarations block .','program',6,'p_program','pascal_sin.py',7),
  ('block -> BEGIN statements END terminator','block',4,'p_block','pascal_sin.py',11),
  ('declarations -> VAR declaration_list ;','declarations',3,'p_declarations','pascal_sin.py',16),
  ('declarations -> CONST declaration_list ;','declarations',3,'p_declarations','pascal_sin.py',17),
  ('declarations -> VAR declaration_list CONST declaration_list','declarations',4,'p_declarations','pascal_sin.py',18),
  ('declarations -> CONST declaration_list VAR declaration_list','declarations',4,'p_declarations','pascal_sin.py',19),
  ('declarations -> <empty>','declarations',0,'p_declarations','pascal_sin.py',20),
  ('declaration_list -> declaration','declaration_list',1,'p_declaration_list','pascal_sin.py',29),
  ('declaration_list -> declaration_list ; declaration','declaration_list',3,'p_declaration_list','pascal_sin.py',30),
  ('declaration -> id_list : type','declaration',3,'p_declaration','pascal_sin.py',37),
  ('id_list -> id','id_list',1,'p_id_list','pascal_sin.py',41),
  ('id_list -> id_list , id','id_list',3,'p_id_list','pascal_sin.py',42),
  ('type -> INTEGER','type',1,'p_type','pascal_sin.py',49),
  ('type -> REAL','type',1,'p_type','pascal_sin.py',50),
  ('type -> STRING','type',1,'p_type','pascal_sin.py',51),
  ('type -> CHAR','type',1,'p_type','pascal_sin.py',52),
  ('type -> BOOLEAN','type',1,'p_type','pascal_sin.py',53),
  ('type -> ARRAY [ expression ] OF type','type',6,'p_type','pascal_sin.py',54),
  ('statements -> statement','statements',1,'p_statements','pascal_sin.py',61),
  ('statements -> statements statement','statements',2,'p_statements','pascal_sin.py',62),
  ('statement -> block','statement',1,'p_statement','pascal_sin.py',69),
  ('statement -> assignment','statement',1,'p_statement','pascal_sin.py',70),
  ('statement -> if_statement','statement',1,'p_statement','pascal_sin.py',71),
  ('statement -> while_statement','statement',1,'p_statement','pascal_sin.py',72),
  ('statement -> for_statement','statement',1,'p_statement','pascal_sin.py',73),
  ('statement -> comments','statement',1,'p_statement','pascal_sin.py',74),
  ('statement -> function_call','statement',1,'p_statement','pascal_sin.py',75),
  ('assignment -> id ASSIGN expression','assignment',3,'p_assignment','pascal_sin.py',79),
  ('if_statement -> IF exprBool THEN statement ifCont','if_statement',5,'p_if_statement','pascal_sin.py',83),
  ('ifCont -> <empty>','ifCont',0,'p_ifCont','pascal_sin.py',91),
  ('ifCont -> ELSE statement','ifCont',2,'p_ifCont','pascal_sin.py',92),
  ('while_statement -> WHILE expression DO statement','while_statement',4,'p_while_statement','pascal_sin.py',101),
  ('for_statement -> FOR id ASSIGN expression forCont','for_statement',5,'p_for_statement','pascal_sin.py',105),
  ('forCont -> TO expression DO statement','forCont',4,'p_forCont','pascal_sin.py',109),
  ('forCont -> DOWNTO expression DO statement','forCont',4,'p_forCont','pascal_sin.py',110),
  ('exprBool -> expression','exprBool',1,'p_exprBool','pascal_sin.py',114),
  ('exprBool -> expression opRel expression','exprBool',3,'p_exprBool','pascal_sin.py',115),
  ('exprBool -> NOT expression','exprBool',2,'p_exprBool','pascal_sin.py',116),
  ('opRel -> =','opRel',1,'p_opRel','pascal_sin.py',125),
  ('opRel -> NOTEQUAL','opRel',1,'p_opRel','pascal_sin.py',126),
  ('opRel -> <','opRel',1,'p_opRel','pascal_sin.py',127),
  ('opRel -> >','opRel',1,'p_opRel','pascal_sin.py',128),
  ('opRel -> MINOREQUALS','opRel',1,'p_opRel','pascal_sin.py',129),
  ('opRel -> LARGEREQUALS','opRel',1,'p_opRel','pascal_sin.py',130),
  ('expression -> term','expression',1,'p_expression','pascal_sin.py',134),
  ('expression -> expression opAdd term','expression',3,'p_expression','pascal_sin.py',135),
  ('expression -> num TWODOTS num','expression',3,'p_expression','pascal_sin.py',136),
  ('opAdd -> +','opAdd',1,'p_opAdd','pascal_sin.py',145),
  ('opAdd -> -','opAdd',1,'p_opAdd','pascal_sin.py',146),
  ('opAdd -> OR','opAdd',1,'p_opAdd','pascal_sin.py',147),
  ('term -> factor','term',1,'p_term','pascal_sin.py',151),
  ('term -> term opMul factor','term',3,'p_term','pascal_sin.py',152),
  ('opMul -> *','opMul',1,'p_opMul','pascal_sin.py',159),
  ('opMul -> /','opMul',1,'p_opMul','pascal_sin.py',160),
  ('opMul -> %','opMul',1,'p_opMul','pascal_sin.py',161),
  ('opMul -> AND','opMul',1,'p_opMul','pascal_sin.py',162),
  ('opMul -> MOD','opMul',1,'p_opMul','pascal_sin.py',163),
  ('opMul -> DIV','opMul',1,'p_opMul','pascal_sin.py',164),
  ('factor -> const terminator','factor',2,'p_factor','pascal_sin.py',168),
  ('factor -> var terminator','factor',2,'p_factor','pascal_sin.py',169),
  ('factor -> function_call','factor',1,'p_factor','pascal_sin.py',170),
  ('factor -> ( exprBool )','factor',3,'p_factor','pascal_sin.py',171),
  ('const -> num','const',1,'p_const','pascal_sin.py',180),
  ('const -> text','const',1,'p_const','pascal_sin.py',181),
  ('const -> TRUE','const',1,'p_const','pascal_sin.py',182),
  ('const -> FALSE','const',1,'p_const','pascal_sin.py',183),
  ('var -> id','var',1,'p_var','pascal_sin.py',187),
  ('var -> id [ expression ]','var',4,'p_var','pascal_sin.py',188),
  ('function_call -> id ( ) terminator','function_call',4,'p_function_call','pascal_sin.py',195),
  ('function_call -> id ( arg_list ) terminator','function_call',5,'p_function_call','pascal_sin.py',196),
  ('terminator -> ;','terminator',1,'p_terminator','pascal_sin.py',203),
  ('terminator -> <empty>','terminator',0,'p_terminator','pascal_sin.py',204),
  ('arg_list -> expression','arg_list',1,'p_arg_list','pascal_sin.py',207),
  ('arg_list -> arg_list , expression','arg_list',3,'p_arg_list','pascal_sin.py',208),
  ('comments -> comment','comments',1,'p_comments','pascal_sin.py',216),
]
