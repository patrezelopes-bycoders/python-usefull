FROM mcr.microsoft.com/dotnet/core/aspnet:2.2-stretch-slim AS base
WORKDIR /app
EXPOSE 80
ARG ENVIRONMENT
ENV ASPNETCORE_ENVIRONMENT=$ENVIRONMENT
ENV RELDEB = RUN IF [ $ASPNETCORE_ENVIRONMENT = "Docker" ] ;then dotnet build "PROJETO" -c "Release" -o /app/buildFROM mcr.microsoft.com/dotnet/core/aspnet:2.2-stretch-slim AS base "Debug"
RUN
WORKDIR /app
EXPOSE 80
ARG ENVIRONMENT
ENV ASPNETCORE_ENVIRONMENT=$ENVIRONMENT
ENV RELDEB = RUN IF [ $ASPNETCORE_ENVIRONMENT = "Docker" ] ;then "Release"  ; else "Debug" ; fi
RUN dotnet build "PROJETO" -c $RELDEB -o /app/build