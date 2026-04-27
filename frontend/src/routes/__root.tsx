import Navbar from "@/components/layout/navbar";
import { createRootRoute, Outlet } from "@tanstack/react-router";

export const Route = createRootRoute({
  component: () => (
    <>
      {/* TODO: replace placeholder landmarks with real navigation/footer */}
      <Navbar />
      <Outlet />
      <footer />
    </>
  ),
});
