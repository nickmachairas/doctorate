CREATE TABLE projects (
      id            serial
    , source_id     smallint
    , description   text
    , warning       varchar(255)
    , site_name     varchar(255)
    , location      varchar(255)
    , source_ref    varchar(100)
    , dqf           smallint
    , PRIMARY KEY (id)
    , CHECK (dqf IN (0, 1, 2, 3, 4, 5))
);

CREATE TABLE misc (
      id            serial
    , project_id    integer
    , reo_check     bool
    , ts_check      bool
    , ut_boring     bool
    , ut_sound      bool
    , i_code        bool
    , PRIMARY KEY (id)
    , FOREIGN KEY (project_id) REFERENCES projects (id)
        ON UPDATE CASCADE
);