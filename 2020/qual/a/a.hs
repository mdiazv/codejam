import Control.Monad
import Data.List (sort, words, unwords, transpose)
import Data.Set as S (fromList, size)

solve :: Int -> [[Int]] -> [Int]
solve n m = [t, r, c]
  where
    t = sum $ [xs !! k | (xs, k) <- zip m [0..n]]
    r = repeatedRows m
    c = repeatedRows $ transpose m
    repeatedRows = length . filter (/= n) . map (S.size . S.fromList)

hasRepeated :: [Int] -> Bool
hasRepeated xs = any (uncurry (==)) $ zip sxs (tail sxs)
  where sxs = sort xs


main = do
  t <- fmap read getLine :: IO Int
  forM_ [1..t] $ \x -> do
    n <- fmap read getLine :: IO Int
    m <- replicateM n $ fmap (map read . words) getLine :: IO [[Int]]
    putStr $ "Case #" ++ (show x) ++ ": "
    putStrLn $ unwords . map show $ solve n m
