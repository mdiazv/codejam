import Control.Monad
import Data.Text(pack, unpack, replace)

-- Given a number n return n enclosed in n parenthesis
enclosed :: Int -> String
enclosed n = (replicate n '(') ++ (show n) ++ (replicate n ')')

-- Replace every number with its parenthesized version
replaceNumbers :: String -> String
replaceNumbers = foldr (.) id replacements
  where
    replacements :: [String -> String]
    replacements = map replaceDigit [0..9]

    replaceDigit :: Int -> String -> String
    replaceDigit n = unpack . replace (pack $ show n) (pack $ enclosed n) . pack

-- Remove all pairs of ")(" recursively
removeInvalid :: String -> String
removeInvalid s =
  let
    t = unpack . replace (pack ")(") (pack "") . pack $ s
  in
    if s == t then s else removeInvalid t

{- Given a string of digits S, insert a minimum number of opening and closing
 - parentheses into it such that the resulting string is balanced and each
 - digit d is inside exactly d pairs of matching parentheses.
 -
 - https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd27/0000000000209a9f
 -}
parenthesize = removeInvalid . replaceNumbers

main = do
  t <- fmap read getLine :: IO Int
  forM_ [1..t] $ \x -> do
    s <- getLine
    putStrLn $ "Case #" ++ (show x) ++ ": " ++ (parenthesize s)
