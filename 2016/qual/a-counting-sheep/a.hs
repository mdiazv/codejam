
import Data.List


main :: IO()
main = do
  input <- getContents  
  let (t:n) = map read $ lines input :: [Int]
  putStr . unlines $ map format $ zip [1..] $ map solve $ take t n

format :: (Int, Int) -> String
format (k, n)
  | n < 0     = preamble ++ "INSOMNIA"
  | otherwise = preamble ++ show n
    where preamble = "Case #" ++ show k ++ ": "

solve :: Int -> Int
solve 0 = -1
solve n = solve' n 1 []

solve' :: Int -> Int -> [Int] -> Int
solve' n k seen
  | seen == [0..9] = n * (k-1)
  | otherwise      = solve' n (k+1) seen'
  where seen' = sort $ merge (digits $ n*k) seen

digits :: Int -> [Int]
digits n = digits' n []
  where
    digits' :: Int -> [Int] -> [Int]
    digits' 0 ds = ds
    digits' n ds = digits' (n `div` 10) $ add_unique (n `mod` 10) ds

merge :: [Int] -> [Int] -> [Int]
merge xs ys = foldr add_unique ys xs

add_unique :: Int -> [Int] -> [Int]
add_unique n xs = add_unique' n xs
  where
    add_unique' :: Int -> [Int] -> [Int]
    add_unique' n [] = (n:xs)
    add_unique' n (y:ys)
      | n == y    = xs
      | otherwise = add_unique' n ys
