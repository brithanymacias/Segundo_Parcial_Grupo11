USE [SAT]
GO

/****** Object:  Table [dbo].[Tramite]    Script Date: 8/2/2026 17:17:36 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[Tramite](
	[CodTramite] [varchar](3) NOT NULL,
	[Descripcion] [varchar](60) NOT NULL,
	[Costo] [decimal](6, 2) NOT NULL,
	[IdCiudadano] [varchar](10) NOT NULL,
	[Nombre] [varchar](60) NOT NULL,
	[Apellido] [varchar](60) NOT NULL,
 CONSTRAINT [PK__Tramite__6DB5168511B97E3F] PRIMARY KEY CLUSTERED 
(
	[CodTramite] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

