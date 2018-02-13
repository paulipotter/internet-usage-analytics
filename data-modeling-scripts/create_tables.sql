-- ****************** SqlDBM: Microsoft SQL Server ******************
-- ******************************************************************

DROP TABLE [activities_recurrence];
GO


DROP TABLE [scams];
GO


DROP TABLE [smartphones];
GO


DROP TABLE [cellphones];
GO


DROP TABLE [tablets];
GO


DROP TABLE [laptops];
GO


DROP TABLE [pcs];
GO


DROP TABLE [city_entry];
GO


DROP TABLE [entries];
GO


DROP TABLE [City];
GO


DROP TABLE [activity];
GO


DROP TABLE [trust_level];
GO


DROP TABLE [scam_type];
GO


DROP TABLE [news_source];
GO


DROP TABLE [social_media];
GO


DROP TABLE [days_recurrence];
GO


DROP TABLE [binary_entries];
GO


DROP TABLE [department];
GO


--************************************** [activity]

CREATE TABLE [activity]
(
 [activity_id] INT NOT NULL ,
 [name]        VARCHAR(50) NOT NULL ,

 CONSTRAINT [PK_activities] PRIMARY KEY CLUSTERED ([activity_id] ASC)
);
GO



--************************************** [trust_level]

CREATE TABLE [trust_level]
(
 [trust_level_id] INT NOT NULL ,
 [level]          VARBINARY(50) NOT NULL ,

 CONSTRAINT [PK_trust_level] PRIMARY KEY CLUSTERED ([trust_level_id] ASC)
);
GO



--************************************** [scam_type]

CREATE TABLE [scam_type]
(
 [scam_type_id] INT NOT NULL ,
 [trust_level]  VARCHAR(50) NOT NULL ,

 CONSTRAINT [PK_scam_type] PRIMARY KEY CLUSTERED ([scam_type_id] ASC)
);
GO



--************************************** [news_source]

CREATE TABLE [news_source]
(
 [news_source_id] INT NOT NULL ,
 [name]           VARCHAR(50) NOT NULL ,

 CONSTRAINT [PK_news_source] PRIMARY KEY CLUSTERED ([news_source_id] ASC)
);
GO



--************************************** [social_media]

CREATE TABLE [social_media]
(
 [social_media_id] INT NOT NULL ,
 [name]            VARBINARY(50) NOT NULL ,

 CONSTRAINT [PK_social_media] PRIMARY KEY CLUSTERED ([social_media_id] ASC)
);
GO



--************************************** [days_recurrence]

CREATE TABLE [days_recurrence]
(
 [recurrence_id] INT NOT NULL ,
 [recurrence]    VARCHAR(50) NOT NULL ,

 CONSTRAINT [PK_days_recurrence] PRIMARY KEY CLUSTERED ([recurrence_id] ASC)
);
GO



--************************************** [binary_entries]

CREATE TABLE [binary_entries]
(
 [bin_id] INT NOT NULL ,
 [answer] VARCHAR(50) NOT NULL ,

 CONSTRAINT [PK_binary_entries] PRIMARY KEY CLUSTERED ([bin_id] ASC)
);
GO



--************************************** [department]

CREATE TABLE [department]
(
 [department_id] INT NOT NULL ,
 [name]          VARCHAR(50) NOT NULL ,

 CONSTRAINT [PK_city_zone] PRIMARY KEY CLUSTERED ([department_id] ASC)
);
GO



--************************************** [entries]

CREATE TABLE [entries]
(
 [entry_id]       INT NOT NULL ,
 [household_size] INT NOT NULL ,
 [social_media]   INT NOT NULL ,
 [news_source]    INT NOT NULL ,
 [internet_trust] INT NOT NULL ,

 CONSTRAINT [PK_entries] PRIMARY KEY CLUSTERED ([entry_id] ASC),
 CONSTRAINT [FK_190] FOREIGN KEY ([social_media])
  REFERENCES [social_media]([social_media_id]),
 CONSTRAINT [FK_199] FOREIGN KEY ([news_source])
  REFERENCES [news_source]([news_source_id]),
 CONSTRAINT [FK_242] FOREIGN KEY ([internet_trust])
  REFERENCES [trust_level]([trust_level_id])
);
GO


CREATE NONCLUSTERED INDEX [fkIdx_190] ON [entries] 
 (
  [social_media] ASC
 )

GO

CREATE NONCLUSTERED INDEX [fkIdx_199] ON [entries] 
 (
  [news_source] ASC
 )

GO

CREATE NONCLUSTERED INDEX [fkIdx_242] ON [entries] 
 (
  [internet_trust] ASC
 )

GO


--************************************** [City]

CREATE TABLE [City]
(
 [city_id]       INT NOT NULL ,
 [name]          VARCHAR(50) NOT NULL ,
 [department_id] INT NOT NULL ,

 CONSTRAINT [PK_City] PRIMARY KEY CLUSTERED ([city_id] ASC),
 CONSTRAINT [FK_23] FOREIGN KEY ([department_id])
  REFERENCES [department]([department_id])
);
GO


CREATE NONCLUSTERED INDEX [fkIdx_23] ON [City] 
 (
  [department_id] ASC
 )

GO


--************************************** [activities_recurrence]

CREATE TABLE [activities_recurrence]
(
 [entry_id]   INT NOT NULL ,
 [activity]   INT NOT NULL ,
 [recurrence] INT NOT NULL ,

 CONSTRAINT [PK_activities_recurrence] PRIMARY KEY CLUSTERED ([entry_id] ASC),
 CONSTRAINT [FK_246] FOREIGN KEY ([entry_id])
  REFERENCES [entries]([entry_id]),
 CONSTRAINT [FK_251] FOREIGN KEY ([recurrence])
  REFERENCES [days_recurrence]([recurrence_id]),
 CONSTRAINT [FK_260] FOREIGN KEY ([activity])
  REFERENCES [activity]([activity_id])
);
GO


CREATE NONCLUSTERED INDEX [fkIdx_246] ON [activities_recurrence] 
 (
  [entry_id] ASC
 )

GO

CREATE NONCLUSTERED INDEX [fkIdx_251] ON [activities_recurrence] 
 (
  [recurrence] ASC
 )

GO

CREATE NONCLUSTERED INDEX [fkIdx_260] ON [activities_recurrence] 
 (
  [activity] ASC
 )

GO


--************************************** [scams]

CREATE TABLE [scams]
(
 [entry_id]  INT NOT NULL ,
 [reported]  INT NOT NULL ,
 [scam_type] INT NOT NULL ,

 CONSTRAINT [PK_scams] PRIMARY KEY CLUSTERED ([entry_id] ASC),
 CONSTRAINT [FK_209] FOREIGN KEY ([entry_id])
  REFERENCES [entries]([entry_id]),
 CONSTRAINT [FK_213] FOREIGN KEY ([reported])
  REFERENCES [binary_entries]([bin_id]),
 CONSTRAINT [FK_222] FOREIGN KEY ([scam_type])
  REFERENCES [scam_type]([scam_type_id])
);
GO


CREATE NONCLUSTERED INDEX [fkIdx_209] ON [scams] 
 (
  [entry_id] ASC
 )

GO

CREATE NONCLUSTERED INDEX [fkIdx_213] ON [scams] 
 (
  [reported] ASC
 )

GO

CREATE NONCLUSTERED INDEX [fkIdx_222] ON [scams] 
 (
  [scam_type] ASC
 )

GO


--************************************** [smartphones]

CREATE TABLE [smartphones]
(
 [entry_id] INT NOT NULL ,
 [utilize]  INT NOT NULL ,
 [home]     INT NOT NULL ,
 [quantity] INT NOT NULL ,

 CONSTRAINT [PK_smartphones] PRIMARY KEY CLUSTERED ([entry_id] ASC),
 CONSTRAINT [FK_106] FOREIGN KEY ([entry_id])
  REFERENCES [entries]([entry_id]),
 CONSTRAINT [FK_131] FOREIGN KEY ([home])
  REFERENCES [binary_entries]([bin_id]),
 CONSTRAINT [FK_135] FOREIGN KEY ([utilize])
  REFERENCES [binary_entries]([bin_id])
);
GO


CREATE NONCLUSTERED INDEX [fkIdx_106] ON [smartphones] 
 (
  [entry_id] ASC
 )

GO

CREATE NONCLUSTERED INDEX [fkIdx_131] ON [smartphones] 
 (
  [home] ASC
 )

GO

CREATE NONCLUSTERED INDEX [fkIdx_135] ON [smartphones] 
 (
  [utilize] ASC
 )

GO


--************************************** [cellphones]

CREATE TABLE [cellphones]
(
 [entry_id] INT NOT NULL ,
 [utilize]  INT NOT NULL ,
 [home]     INT NOT NULL ,
 [quantity] INT NOT NULL ,

 CONSTRAINT [PK_cellphones] PRIMARY KEY CLUSTERED ([entry_id] ASC),
 CONSTRAINT [FK_101] FOREIGN KEY ([entry_id])
  REFERENCES [entries]([entry_id]),
 CONSTRAINT [FK_123] FOREIGN KEY ([home])
  REFERENCES [binary_entries]([bin_id]),
 CONSTRAINT [FK_127] FOREIGN KEY ([utilize])
  REFERENCES [binary_entries]([bin_id])
);
GO


CREATE NONCLUSTERED INDEX [fkIdx_101] ON [cellphones] 
 (
  [entry_id] ASC
 )

GO

CREATE NONCLUSTERED INDEX [fkIdx_123] ON [cellphones] 
 (
  [home] ASC
 )

GO

CREATE NONCLUSTERED INDEX [fkIdx_127] ON [cellphones] 
 (
  [utilize] ASC
 )

GO


--************************************** [tablets]

CREATE TABLE [tablets]
(
 [entry_id] INT NOT NULL ,
 [utilize]  INT NOT NULL ,
 [home]     INT NOT NULL ,
 [quantity] INT NOT NULL ,

 CONSTRAINT [PK_tablets] PRIMARY KEY CLUSTERED ([entry_id] ASC),
 CONSTRAINT [FK_96] FOREIGN KEY ([entry_id])
  REFERENCES [entries]([entry_id]),
 CONSTRAINT [FK_119] FOREIGN KEY ([utilize])
  REFERENCES [binary_entries]([bin_id]),
 CONSTRAINT [FK_174] FOREIGN KEY ([home])
  REFERENCES [binary_entries]([bin_id])
);
GO


CREATE NONCLUSTERED INDEX [fkIdx_96] ON [tablets] 
 (
  [entry_id] ASC
 )

GO

CREATE NONCLUSTERED INDEX [fkIdx_119] ON [tablets] 
 (
  [utilize] ASC
 )

GO

CREATE NONCLUSTERED INDEX [fkIdx_174] ON [tablets] 
 (
  [home] ASC
 )

GO


--************************************** [laptops]

CREATE TABLE [laptops]
(
 [entry_id]      INT NOT NULL ,
 [utilize]       INT NOT NULL ,
 [home]          INT NOT NULL ,
 [quantity]      INT NOT NULL ,
 [recurrence_id] INT NOT NULL ,

 CONSTRAINT [PK_laptops] PRIMARY KEY CLUSTERED ([entry_id] ASC),
 CONSTRAINT [FK_62] FOREIGN KEY ([entry_id])
  REFERENCES [entries]([entry_id]),
 CONSTRAINT [FK_79] FOREIGN KEY ([home])
  REFERENCES [binary_entries]([bin_id]),
 CONSTRAINT [FK_83] FOREIGN KEY ([utilize])
  REFERENCES [binary_entries]([bin_id]),
 CONSTRAINT [FK_154] FOREIGN KEY ([recurrence_id])
  REFERENCES [days_recurrence]([recurrence_id])
);
GO


CREATE NONCLUSTERED INDEX [fkIdx_62] ON [laptops] 
 (
  [entry_id] ASC
 )

GO

CREATE NONCLUSTERED INDEX [fkIdx_79] ON [laptops] 
 (
  [home] ASC
 )

GO

CREATE NONCLUSTERED INDEX [fkIdx_83] ON [laptops] 
 (
  [utilize] ASC
 )

GO

CREATE NONCLUSTERED INDEX [fkIdx_154] ON [laptops] 
 (
  [recurrence_id] ASC
 )

GO


--************************************** [pcs]

CREATE TABLE [pcs]
(
 [entry_id]      INT NOT NULL ,
 [utilize]       INT NOT NULL ,
 [home]          INT NOT NULL ,
 [quantity]      INT NOT NULL ,
 [recurrence_id] INT NULL ,

 CONSTRAINT [PK_pcs] PRIMARY KEY CLUSTERED ([entry_id] ASC),
 CONSTRAINT [FK_48] FOREIGN KEY ([entry_id])
  REFERENCES [entries]([entry_id]),
 CONSTRAINT [FK_71] FOREIGN KEY ([utilize])
  REFERENCES [binary_entries]([bin_id]),
 CONSTRAINT [FK_75] FOREIGN KEY ([home])
  REFERENCES [binary_entries]([bin_id]),
 CONSTRAINT [FK_150] FOREIGN KEY ([recurrence_id])
  REFERENCES [days_recurrence]([recurrence_id])
);
GO


CREATE NONCLUSTERED INDEX [fkIdx_48] ON [pcs] 
 (
  [entry_id] ASC
 )

GO

CREATE NONCLUSTERED INDEX [fkIdx_71] ON [pcs] 
 (
  [utilize] ASC
 )

GO

CREATE NONCLUSTERED INDEX [fkIdx_75] ON [pcs] 
 (
  [home] ASC
 )

GO

CREATE NONCLUSTERED INDEX [fkIdx_150] ON [pcs] 
 (
  [recurrence_id] ASC
 )

GO


--************************************** [city_entry]

CREATE TABLE [city_entry]
(
 [city_id]  INT NOT NULL ,
 [entry_id] INT NOT NULL ,

 CONSTRAINT [PK_city_entry] PRIMARY KEY CLUSTERED ([city_id] ASC, [entry_id] ASC),
 CONSTRAINT [FK_27] FOREIGN KEY ([city_id])
  REFERENCES [City]([city_id]),
 CONSTRAINT [FK_39] FOREIGN KEY ([entry_id])
  REFERENCES [entries]([entry_id])
);
GO


CREATE NONCLUSTERED INDEX [fkIdx_27] ON [city_entry] 
 (
  [city_id] ASC
 )

GO

CREATE NONCLUSTERED INDEX [fkIdx_39] ON [city_entry] 
 (
  [entry_id] ASC
 )

GO


