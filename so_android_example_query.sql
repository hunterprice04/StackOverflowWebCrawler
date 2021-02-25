-- https://data.stackexchange.com/stackoverflow/queries
-- this post will return ~50000 posts with their id's that you can
-- append to the end of this url 'https://stackoverflow.com/questions/'
-- to get the url of a stackoverflow post that has an android tag
-- this is only an example data set because it will only get posts
-- within the last 2 years
SELECT Id, Title, Body
FROM Posts
WHERE Tags LIKE '%android%' AND CreationDate >= '2019-02-24';