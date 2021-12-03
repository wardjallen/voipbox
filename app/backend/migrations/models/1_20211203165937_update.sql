-- upgrade --
CREATE TABLE IF NOT EXISTS "clusters" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "clusterName" VARCHAR(64) NOT NULL UNIQUE,
    "clusterAxlUsername" VARCHAR(255),
    "clusterAxlPassword" VARCHAR(255),
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "modified_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP
);
-- downgrade --
DROP TABLE IF EXISTS "clusters";
