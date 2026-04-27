import Navbar from "@/components/layout/navbar";
import { createRootRoute, Outlet } from "@tanstack/react-router";

export const Route = createRootRoute({
  component: () => (
    <>
      <div className="absolute top-0 left-0 right-0 z-50">
        <Navbar />
      </div>
      <Outlet />
      <footer />
    </>
  ),
});
