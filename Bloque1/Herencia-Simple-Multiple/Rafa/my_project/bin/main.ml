class person (name: string) = object
  val mutable _name = name
  method get_name = name
end;;

class student (name: string) = object
  inherit person name
  method study = print_endline (_name ^ " esta estudiando")
end;;

class teacher (name: string) = object
  inherit person name
  method teach = print_endline (_name ^ " esta enseñando")
end;;

let emilio = new student "Emilio";;
emilio#study;;

let mag = new teacher "Mag";;
mag#teach;;

class swimmer = object
  method swim = print_endline "swimming"
end;;

class cyclist = object
  method pedal = print_endline "pedaleando"
end;;

class runner = object
  method run = print_endline "logging in strava"
end;;

class triathlete = object
  inherit swimmer
  inherit cyclist
  inherit runner
  method compete = print_endline "compitiendo"
end;;

let t = new triathlete;;

let () = print_endline "El triatleta";;
t#swim;;
t#pedal;;
t#run;;
t#compete;;

class animal = object
  method eat = print_endline "comiendo"
end;;

class mammal = object
  inherit animal
  method feed_offspring = print_endline "alimentando crias"
end;;

class dog = object
  inherit mammal
  method bark = print_endline "woof"
end;;

let maka = new dog;;
maka#eat;;
maka#feed_offspring;;
maka#bark;;

class worker (name: string) (income: float) = object
  val mutable name = name
  val mutable income = income

  method get_name = name
  method get_income = income
end;;

class chief (name: string) (income: float) = object
  inherit worker name income
  method manage_team = print_endline "dirigiendo equipo"
end;;

class programmer (name: string) (income: float) = object
  inherit worker name income
  method code = print_endline "programando"
end;;

class accountant (name: string) (income:float) = object
  inherit worker name income
  method manage_accounts = print_endline "contando"
end;;

let jessica = new chief "Jesica" 100.5;;
let fernando = new programmer "Fernando" 50.5;;
let jair = new accountant "Jair" 20.5;;

print_endline jessica#get_name;;
jessica#manage_team;;
print_endline (string_of_float jessica#get_income);;

print_endline fernando#get_name;;
fernando#code;;
print_endline (string_of_float fernando#get_income);;

print_endline jair#get_name;;
jair#manage_accounts;;
print_endline (string_of_float jair#get_income);;

