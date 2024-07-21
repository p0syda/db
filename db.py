-- база данных

-- Таблица жанров
CREATE TABLE Genres (
    ID SERIAL PRIMARY KEY,
    Name VARCHAR(255) NOT NULL
);

-- Таблица исполнителей
CREATE TABLE Artists (
    ID SERIAL PRIMARY KEY,
    Name VARCHAR(255) NOT NULL
);

-- Таблица связи исполнителей и жанров
CREATE TABLE ArtistGenres (
    ArtistID INT,
    GenreID INT,
    FOREIGN KEY (ArtistID) REFERENCES Artists(ID),
    FOREIGN KEY (GenreID) REFERENCES Genres(ID),
    PRIMARY KEY (ArtistID, GenreID)
);

-- Таблица альбомов
CREATE TABLE Albums (
    ID SERIAL PRIMARY KEY,
    Title VARCHAR(255) NOT NULL,
    ReleaseYear INT
);

-- Таблица связи исполнителей и альбомов
CREATE TABLE ArtistAlbums (
    ArtistID INT,
    AlbumID INT,
    FOREIGN KEY (ArtistID) REFERENCES Artists(ID),
    FOREIGN KEY (AlbumID) REFERENCES Albums(ID),
    PRIMARY KEY (ArtistID, AlbumID)
);

-- Таблица треков
CREATE TABLE Tracks (
    ID SERIAL PRIMARY KEY,
    Title VARCHAR(255) NOT NULL,
    Duration TIME,
    AlbumID INT,
    FOREIGN KEY (AlbumID) REFERENCES Albums(ID)
);

-- Таблица сборников
CREATE TABLE Compilations (
    ID SERIAL PRIMARY KEY,
    Title VARCHAR(255) NOT NULL,
    ReleaseYear INT
);

-- Таблица связи сборников и треков
CREATE TABLE CompilationTracks (
    CompilationID INT,
    TrackID INT,
    FOREIGN KEY (CompilationID) REFERENCES Compilations(ID),
    FOREIGN KEY (TrackID) REFERENCES Tracks(ID),
    PRIMARY KEY (CompilationID, TrackID)
);