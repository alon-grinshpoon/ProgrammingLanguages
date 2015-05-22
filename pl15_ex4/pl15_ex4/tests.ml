(*
  Tests for the lambda calculus parser and reducers.

  EXTEND THIS FILE TO TEST YOUR SOLUTION THOROUGHLY!
*)

open Core.Std

open Parser
open Reducer


let rec evaluate ~verbose reduce t =
  if verbose then print_string (format_term t) else ();
  match reduce t with
  | None -> 
    if verbose then print_string " =/=>\n\n" else ();
    t
  | Some t' -> 
    if verbose then print_string " ==>\n\n" else ();
    evaluate ~verbose reduce t'


let s1 = "
let tru = (\\t.(\\f.t)) in
let fls = (\\t.(\\f.f)) in
let and = (\\b.(\\c. ((b c) fls))) in
((and tru) tru)
"


let s2 = "
let tru = (\\t.(\\f.t)) in
let fls = (\\t.(\\f.f)) in
let and = (\\b.(\\c. ((b c) fls))) in
((and fls) tru)
"


let () =
  printf "\nEvaluating:\n%s\nin lazy semantics:\n\n" s1;
  ignore (evaluate ~verbose:true reduce_lazy (parse s1));
  printf "\n\nEvaluating:\n%s\nin strict semantics:\n\n" s2;
  ignore (evaluate ~verbose:true reduce_strict (parse s2));
  printf "\n\nEvaluating:\n%s\nin normal-order semantics:\n\n" s2;
  ignore (evaluate ~verbose:true reduce_normal (parse s2));
