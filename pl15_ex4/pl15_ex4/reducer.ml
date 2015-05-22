(*
  Reducers (interpreters) for lambda-calculus.
*)

open Core.Std

open Parser


exception OutOfVariablesError


let possible_variables = List.map ~f:(fun x -> Char.to_string (char_of_int x)) ((List.range 97 123) @ (List.range 65 91))


(*
  ADD FUNCTIONS BELOW
*)
