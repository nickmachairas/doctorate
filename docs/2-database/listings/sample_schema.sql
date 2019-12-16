CREATE TABLE projects (
      id            serial
    , user_id       integer
    , location_id   integer
    , source_db     varchar(64)
    , source_id     smallint
    , description   text
    , warning       varchar(255)
    , site_name     varchar(128)
    , source_ref    text
    , dqf           smallint
    , contractor    varchar(255)
    , number        varchar(128)
    , title         varchar(255)
    , date_added    date
    , date_modified date DEFAULT NOW()
    , PRIMARY KEY (id)
    , FOREIGN KEY (user_id) REFERENCES users (id),
    , FOREIGN KEY (location_id) REFERENCES locations (id)
);

CREATE TABLE clones (
      org_id    integer
    , new_id    integer
    , PRIMARY KEY (org_id, new_id)
    , FOREIGN KEY (org_id) REFERENCES projects (id)
    , FOREIGN KEY (new_id) REFERENCES projects (id)
);
