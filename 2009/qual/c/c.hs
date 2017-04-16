import Text.Printf (printf)

main :: IO ()
main = do
  first <- getLine
  rest <- getContents
  let t = read first :: Int
  let cases = take t $ lines rest
  putStr . unlines $ zipWith format [1..t] $ map solve cases

solve :: String -> Int
solve = (flip welcome) "welcome to code jam"

format :: Int -> Int -> String
format = printf "Case #%d: %04d"

welcome :: String -> String -> Int
welcome _ [] = 1
welcome [] _ = 0
welcome (x:xs) yss@(y:ys)
  | x == y    = (take + donttake) `mod` 10000
  | otherwise = donttake
  where
    take     = welcome xs ys `mod` 10000
    donttake = welcome xs yss `mod` 10000
