# 04_AUFGABE: komplexe Abfrage
--
-- Datenbank: dbkurs_littlemusic, Tabelle: album, songs
-- 1)
-- Gib in der ersten Spalte den Songnamen und in der zweiten Spalte Namen des Albums aus. Benutze einen Subselect.
SELECT b.title, bs.title 
FROM books AS b
JOIN books_subjects AS bs
    ON bs.id = b.subject_id
WHERE bs.title = 'Love stories';

select s.name as Songtitle, a.name as Albumname
from songs s join album a on a.id =s.album_id